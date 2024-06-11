#!/bin/bash

# This script defines bash functions used by code generation scripts in each lambda folder.
# Functions assume that:
#  SCRIPT_DIR points to the directory containing the xxx-generate.sh script (core or connector/erp_klio_lambda)
#  PROJECT_DIR is the root of the project (AWS_backend) one to three levels above SCRIPT_DIR
#  $(dirname ${SCRIPT_DIR}) with the "_lambda" suffix removed if present, is the API_NAME (core or erp_klio)

#  The OpenAPI file must be ${SCRIPT_DIR}/${API_NAME}-openapi.json
#
#  The Python package defaults to
#  The starting OpenAPI specification file is ${SCRIPT_DIR}/../$(dirname ${SCRIPT_DIR})-openapi.json.
#
# The code will be generated in ${SCRIPT_DIR} (e.g. connector/erp_klio_lambda)
# The API default name will be derived from the target folder name (e.g. erp_klio_lambda -> erp_klio) with the lambda
# suffix removed if any. It can be overridden by passing a parameter $1 to the function. The source OpenApi file
# must be named "${API_NAME}-openapi.json",
#
# Parameters:
# 1:  Server port (mandatory)
# 2:  API path prefix (mandatory, e.g. /core/v1)
# 3:  API name override (optional)
function generate_server_api() {
  local server_port
  local lambda
  local openapi_filename

  server_port="$1"  # e.g. 8080

  if [[ ! "$server_port" =~ ^[0-9]+$ ]]; then
    echo "Error: server port must be an integer"
  fi

  local api_path_prefix
  api_path_prefix="$2"  # e.g. /core/v1

  if [[ ! "$api_path_prefix" =~ ^/ ]]; then
    echo "Error: API path prefix must start with /"
  fi

  if [[ -z "${server_port}" || -z "${api_path_prefix}" ]]; then
    echo "Error: server port and API path prefix must be provided"
  fi

  lambda=$(basename "${SCRIPT_DIR}")  # e.g. core
  export API_NAME=${lambda%_lambda}  # e.g. core
  folder="${SCRIPT_DIR}/api_${API_NAME}_lambda"
  openapi_filename="${SCRIPT_DIR}/${API_NAME}-openapi.json"

  # Eventual override
  API_NAME="${3:-${API_NAME}}"  # e.g. api_python_server

  # Set Python and JAVA versions if unset
  export PYTHON=${PYTHON:-/home/jm/.pyenv/versions/3.11.0/envs/aws-cdk/bin/python3}
  export JAVA=${JAVA:-/snap/pycharm-professional/current/jbr/bin/java}
  export PYTHON_POST_PROCESS_FILE="${PYTHON} core/utils.py run_yapf"

  # Source OpenAPI specification
  OPEN_API_FILE=$(realpath "${openapi_filename}") || ( echo "No API specification ${openapi_filename}" ; exit 21 )

  # Resolve references in the openapi file to get the merged JSON, without external references as "resolved-xxx.json".
  OPEN_API_JSON=$(python3 core/utils.py dereference "${OPEN_API_FILE}")

  # Additional properties
  PROPS="sortParamsByRequiredFlag=true"
  PROPS="${PROPS},sortModelPropertiesByRequiredFlag=true"
  PROPS="${PROPS},ensureUniqueParams=true"
  PROPS="${PROPS},allowUnicodeIdentifiers=false"
  PROPS="${PROPS},legacyDiscriminatorBehavior=true"
  PROPS="${PROPS},enumUnknownDefaultCase=true"
  PROPS="${PROPS},disallowAdditionalPropertiesIfNotPresent=false"
  PROPS="${PROPS},sourceFolder=src"
  PROPS="${PROPS},packageVersion=1.0.0"
  PROPS="${PROPS},packageName=${API_NAME}"
  PROPS="${PROPS},serverPort=${server_port}"

  ${JAVA} --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED \
      -jar /home/jm/.cache/JetBrains/PyCharm2024.1/openapi/codegen/71aab8d6724718f581fedb5bf4fd5866/openapi-generator-cli-6.2.0.jar \
      generate -g python-fastapi \
      -i "${OPEN_API_JSON}" \
      -o "${folder}" --enable-post-process-file \
      --additional-properties="${PROPS}"

  API_NAME="${API_NAME}" fix_fastapi_root_path "${api_path_prefix}" "${folder}/src/${API_NAME}/main.py"
}
# The generated code has a bug that causes the following error: "Path parameters cannot have a default value"
# The root cause is the presence of "None" instead of "..." in the generated code, inside a fastapi.Path object
# constructor,
function fix_fastapi_path() {
    local file_path="$1"

    # Check if the file exists
    if [[ ! -f "$file_path" ]]; then
        echo "Error: File does not exist."
        return 1
    fi

    # Check if 'Path' is imported from 'fastapi' using awk for multiline support
    if ! awk 'BEGIN{RS=""; FS="\n"} /from\s+fastapi\s+import/{if(/Path/){found=1}} END{exit !found}' "$file_path"; then
        echo "Error: 'Path' not imported from 'fastapi' in the file."
        return 1
    fi

    # Perform the replacement
    # This uses -z in sed to treat newline as a regular character, allowing multi-line matching
    sed -i'' -E ':a;N;$!ba;s/Path\((\s*)None(\s*),/Path(\1...\2,/g' "$file_path"

    echo "File '$file_path' has been modified successfully."
}

# The root_path is a parameter of fastapi.FastAPI constructor, which defaults to "/". When the API is intended to
# be served behind a fixed path prefix, the root path must be set to that prefix, so that generated links include
# it.
# 1: root_path="/core/v1" (mandatory)
# 2: target file (mandatory)
function fix_fastapi_root_path() {
  local root_path="$1"
  # check target
  local target="$2"

  if [[ ! -f "$target" ]]; then
    echo "Error: File '${target}' does not exist."
    return 2
  fi
  # add the parameter
  sed -i '/FastAPI(/,/^)/ s#^)#    root_path="'"${root_path}"'",\n)#' "${target}"

  # run yapf to reformat the file
  if [[ -x "${PYTHON}" ]]; then
    ${PYTHON} core/utils.py run_yapf -i "$target"
  fi
}

# This function centralizes edits to generated server code. The first fix is a call to the above function to
# correct the first parameter to fastapi.Path constructor calls. The second fix is more sophisticated and relies
# on the utils.py program's linker function, which imports a file called "implementation.py" and replaces the
# ellipsis in the default implementations by calls to the actual implementation. It is expected that
# "implementation.py" contains only import statements from an organized set of modules covering all the business
# logic of the API.
# 1: path name of api_${API_NAME}_lambda/src/${PACKAGE_NAME}/apis
# 2: prefix of the file in package /apis generated file (e.g. "clients" for apis/clients_api.py).
function finalize_api_file() {
  local package_apis="${1}"
  local file_path="${package_apis}/$2_api.py"
  # Check if the file exists
  if [[ ! -f "$file_path" ]]; then
      echo "Error: File '${file_path}' does not exist."
      return 1
  fi
  # Fix fastapi dialect
  fix_fastapi_path "$file_path"

  # The automatically generated server code has coroutines without a real body.
  # The body is just an ellipsis.
  # This functions uses sister module (handwritten) implementation.py to provide suitable
  # implementation for each function. The implementation module must define functions bearing
  # the same name as the coroutine, with the exact same signature.
  ${PYTHON} core/utils.py linker "$file_path"
}