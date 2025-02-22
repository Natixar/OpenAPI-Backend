""" Module core.utils

    Contains several utility functions used by the application.
    
    - dereference: Reads the named JSON file, resolves all references, saves the resolved file and
                returns the relative path of the resolved JSON file. Supported by the jsonref library.

    - format_md: The CommonMark markdown in most 'description' fields in the OpenApi 3.0 standard
                are not preserved because the lines are concatenated without taking the markdown into
                account. This function detects ### header marks and restores the document structure
                in the autogenerated documentation.
                
    - run_yapf: Some code generators, especially Python ones, do not properly quote the path of the file
                that must be processed by yapf3. The program sees the path broken up as two distinct
                command line arguments when they only expect one. This wrapper concatenates the arguments
                with one space. It cannot guess how many spaces are actually needed.
    
    - linker:   Autogenerated server code ends with *_api.py modules where routes are implemented using
                decorated empty functions. The body is an ellipsis. If the implementation.py module is
                located in the same package, this command replaces the ellipsis with a call to the same
                signature function in the implementation module. The linker is called from generate.sh
                scripts as the final stage of server code generation from the OpenApi specification.
                    Created on 30/04/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
    © Natixar SAS 2024
"""

# Import system libraries
import sys
import os
import ast
import subprocess
import urllib.request
from typing import TypeVar, LiteralString, Optional, cast, Any
from urllib.parse import urljoin

# Import public libraries
import jsonref
from more_itertools import peekable

# Import application modules

FilePath = TypeVar('FilePath', str, LiteralString, os.PathLike)


#@overload
def dereference(filepath: FilePath, base_uri: Optional[str] = None) -> FilePath:
    """
    Reads the named JSON file, resolves all references, saves the resolved file and
    returns the relative path of the resolved JSON file. Supported by the jsonref library.

    :param filepath: the JSON file to resolve
    :param base_uri: the prefix to add to relative references, defaults to the directory containing the file `filepath`
    :return: the relative path of the resolved JSON file
    :raises JSONDecodeError: if the input JSON is invalid.
    :raises JsonRefError: if the referenced file contains invalid JSON, cannot be found or if the
            reference itself is an invalid URI.
    """
    # Separate the path from the filename
    path, filename = os.path.split(filepath)
    if base_uri is None:
        # urljoin() in jsonref only keeps the "base" argument until the last slash, so we need to
        # compute the absolute path of the file to get the full URI.
        absolute_path = os.path.abspath(path)
        if not absolute_path.endswith('/'):
            absolute_path += '/'
        base_uri = urljoin('file:', urllib.request.pathname2url(absolute_path))
    # Compute result filename on the model "resolved-" + filename
    result_filename = os.path.join(path, f"resolved-{filename:s}")
    with open(filepath, 'r') as f:
        data = jsonref.load(f, base_uri=base_uri)
    # Dereferencing is actually performed lazily while serializing the output
    with open(result_filename, 'w') as f:
        jsonref.dump(data, f, indent=2)  # May throw TypeError
    
    return os.path.relpath(result_filename)

def format_markdown(filepath_in: FilePath, filepath_out: Optional[FilePath]=None):
    """
    Reads the named markdown file looks for paragraphs of CommonMark concatenated on one line
    and split it over several lines.

    :param filepath_in: the input file
    :param filepath_out: the optional output file. If omitted, print on stdout.
    """
    with open(filepath_in, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    for line in lines:
        # Focus on CommonMark title lines
        if line[:3] == "###" and " ### " in line[5:]:
            parts = line[3:].split("###")
            for part in parts:
                # Break down by word and detect Title Case header
                words = part.split(" ")
                # Find first "significant" all lower case word
                for i, w in enumerate(words):
                    if len(w) >= 4 and w.islower():
                        #print(w)
                        # Find preceding capitalized word
                        for j, start_word in enumerate(words[i::-1]):
                            if start_word and start_word[0].isupper():
                                # Found: cut part at j
                                processed_lines.append("####" + " ".join(words[:j+1]) + "\n")
                                processed_lines.append(" ".join(words[j+1:]) + "\n\n")
                                break
                        else:
                            # Not found: nothing is capitalized. keep first (non-empty) word as title (fallback)
                            processed_lines.append("#### " + next(filter(lambda w: bool(w), words)) + "\n")
                        break
                else:
                    # Keep everything as title
                    processed_lines.append("####" + part + "\n")
            continue  # with next line
        # Fallback: normal line
        processed_lines.append(line)
    
    if filepath_out is None:
        print(''.join(processed_lines))
    else:
        with open(filepath_out, 'w', encoding='utf-8') as file:
            file.write(''.join(processed_lines))
            

def run_yapf(args) -> None:
    """ Compensates a bug in the code generator OpenApi Codegen 6, which fails to properly
        quote the path of the file to be formatted when calling the Python formatting command (usually yapf).
        
    :param args: the file path spread over one or several arguments
    :return: None
    """
    # Join the arguments to form the complete file path
    file_path = " ".join(args)
    command = ['/usr/bin/yapf3', '-i', file_path]

    try:
        # Execute the command
        subprocess.run(command, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running YAPF: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    else:
        print(f"Reformatted '{file_path}'")
        
        
def linker(target_api: FilePath):
    """
    Autogenerated server code ends with *_api.py modules where routes are implemented using
    decorated empty functions. The body is an ellipsis. If the implementation.py module is
    located in the same package, this command replaces the ellipsis with a call to the same
    signature function in the implementation module. The linker is called from generate.sh
    scripts as the final stage of server code generation from the OpenApi specification.

    :param target_api: the path to the *_api.py file
    :return: None
    """
    import astor
    
    def replace_ellipsis_with_impl(source_file):
        with open(source_file, "r") as source:
            tree = ast.parse(source.read(), filename=source_file)
    
        imports = []
        class EllipsisReplacer(ast.NodeTransformer):
            def process_function_def(self, node, mode_async: bool=False):
                # Check if the body of the function is a single Ellipsis node
                if len(node.body) <= 2 and isinstance(node.body[-1], ast.Expr):
                    # When length is 2, check if the first node is a comment string constant
                    if not isinstance(node.body[0], ast.Expr):
                        return node
                    expr = cast(ast.Expr, node.body[0]).value
                    if not isinstance(expr, ast.Constant) or not isinstance(expr.value, str):
                        return node
                    # Now focus on the last statement
                    if not isinstance(node.body[-1], ast.Expr):
                        return node
                    expr = cast(ast.Expr, node.body[-1]).value
                    if isinstance(expr, ast.Constant) and expr.value is ...:
                        # Prepare the replacement code with the correct function name and import modifications
                        print(f"Found ... at line {node.body[-1].lineno}.")
                        # Prepare positional and keyword arguments from the api
                        # In the FunctionDef, arguments is:
                        # (arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs, expr* kw_defaults, arg? kwarg, expr* defaults)
                        # For each ``arg``, we need the identifier which is ``arg.arg``.
                        # The function call is simpler, made only of args (expressions) and kwargs (arg=expression).
                        # The posonlyargs go into args as arg.arg
                        args: list[Any] = [ast.Name(id=arg.arg, ctx=ast.Load()) for arg in node.args.posonlyargs]
                        # The args (not position only) go into keywords.
                        keywords = [ast.keyword(arg=arg.arg, value=ast.Name(id=arg.arg, ctx=ast.Load())) for arg in node.args.args]
                        # The vararg, if present, goes into args as an expression ast.Starred
                        if node.args.vararg:
                            args.append(ast.Starred(value=ast.Name(id=node.args.vararg, ctx=ast.Load()), ctx=ast.Load()))
                        # The kwonlyargs and kwarg go into keywords too
                        if node.args.kwonlyargs:
                            keywords.extend([ast.keyword(arg=arg.arg, value=ast.Name(id=arg.arg, ctx=ast.Load()), ctx=ast.Load())
                                             for arg in node.args.kwonlyargs])
                        if node.args.kwarg:
                            keywords.extend([ast.keyword(arg=arg.arg, value=ast.Name(id=arg.arg, ctx=ast.Load()), ctx=ast.Load())
                                             for arg in node.args.kwarg])

                        text_call = f"return {'await ' if mode_async else ' '}{node.name}_impl()"
                        return_statement = cast(ast.Return, ast.parse(text_call).body[0])
                        if isinstance(return_statement.value, ast.Await):
                            call = return_statement.value.value
                        else:
                            call = return_statement.value
                        call.args = args
                        call.keywords = keywords
                        # Replace the ellipsis with the call to the implementation function
                        node.body[-1] = return_statement
                        # Import implementation
                        imports.append(node.name)
                # Recursively process the function definition
                self.generic_visit(node)
                return node

            def visit_FunctionDef(self, node):
                return self.process_function_def(node)

            def visit_AsyncFunctionDef(self, node):
                # Same processing
                return self.process_function_def(node, mode_async=True)
        
        tree = EllipsisReplacer().visit(tree)
        ast.fix_missing_locations(tree)
    
        # Extract namespace package name from ``target_api``
        package = target_api.split(os.sep)[3]
        with open(source_file, "w") as output:
            # Write "from implementation import funcname as funcname_impl" lines
            for function_name in imports:
                output.write(f"from {package}.implementation import {function_name} as {function_name}_impl\n")
            output.write(astor.to_source(tree))
            
    replace_ellipsis_with_impl(target_api)
    run_yapf([target_api])
            
# Run the module as a program, with arguments for filepath and base_uri
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: dereference.py <command> <filepath> [<base_uri>]')
        sys.exit(0)
    if sys.argv[1] == 'dereference':
        if len(sys.argv) < 3 or len(sys.argv) > 4:
            print('Usage: python3 utils.py dereference.py dereference <filepath> [<base_uri>]')
            sys.exit(0)
        filepath = sys.argv[2]
        base_uri = sys.argv[3] if len(sys.argv) == 4 else None
        print(dereference(filepath, base_uri))
    elif sys.argv[1] == 'format_md':
        if len(sys.argv) != 3:
            print("Usage: python3 utils.py format_md <filepath>")
            sys.exit(0)
        filepath_in = sys.argv[2]
        filepath_out = sys.argv[3] if len(sys.argv) > 3 else filepath_in
        format_markdown(filepath_in, filepath_out)
    elif sys.argv[1] == 'run_yapf':
        if len(sys.argv) <= 2:
            print("Usage: python3 utils.py run_yapf <quoted filepath> [additional unquoted bits]")
            sys.exit(0)
    elif sys.argv[1] == 'linker':
        if len(sys.argv) != 3:
            print("Usage: python3 utils.py linker <filepath>")
            sys.exit(0)
        linker(sys.argv[2])
    else:
        print("Commands: dereference format_md run_yapf linker")
        sys.exit(1)
    