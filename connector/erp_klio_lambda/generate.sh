#!/bin/bash

SCRIPT_DIR="$(dirname "$0")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/../..")"
cd "${PROJECT_DIR}" || exit

PYTHON=/home/jm/.pyenv/versions/3.11.0/envs/aws-cdk/bin/python3

export PYTHON_POST_PROCESS_FILE="${PYTHON} core/utils.py run_yapf"

# Resolve references
OPEN_API_JSON=$(python3 core/utils.py dereference "connector/erp-klio-openapi.json")

JAVA=/snap/pycharm-professional/387/jbr/bin/java
${JAVA} -jar /home/jm/.cache/JetBrains/PyCharm2024.1/openapi/codegen/71aab8d6724718f581fedb5bf4fd5866/openapi-generator-cli-6.2.0.jar generate -g python-fastapi \
     -i "${OPEN_API_JSON}" \
     -o "connector/erp_klio_lambda" --enable-post-process-file \
     --additional-properties=sortParamsByRequiredFlag=true,sortModelPropertiesByRequiredFlag=true,ensureUniqueParams=true,allowUnicodeIdentifiers=false,legacyDiscriminatorBehavior=true,enumUnknownDefaultCase=true,disallowAdditionalPropertiesIfNotPresent=false,sourceFolder=src,packageVersion=1.0.0,packageName=erp_klio_python_server,serverPort=8080

# Automated code updates

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

    echo "File has been modified successfully."
}

# Fix files
fix_fastapi_path "connector/erp_klio_lambda/src/erp_klio_python_server/apis/default_api.py"

# The automatically generated server code has coroutines without a real body.
# The body is just an ellipsis.
# This functions uses sister module (handwritten) implementation.py to provide suitable
# implementation for each function. The implementation module must define functions bearing
# the same name as the coroutine, with the exact same signature.
${PYTHON} core/utils.py linker "connector/erp_klio_lambda/src/erp_klio_python_server/apis/default_api.py"

# Automated improvements of docs: if needed, see tests/connectors/erp-klio/generate.sh
