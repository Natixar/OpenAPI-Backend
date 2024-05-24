#!/bin/bash

SCRIPT_DIR="$(dirname "$0")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/../..")"
cd "${PROJECT_DIR}" || exit

OPEN_API_JSON="connector/utility-grdf-1.6.json"

export PYTHON_POST_PROCESS_FILE="${PYTHON} core/utils.py run_yapf"

JAVA=/snap/pycharm-professional/387/jbr/bin/java
${JAVA} --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED \
        -jar /home/jm/.cache/JetBrains/PyCharm2024.1/openapi/codegen/71aab8d6724718f581fedb5bf4fd5866/openapi-generator-cli-6.2.0.jar generate \
        -g python \
        -i "${OPEN_API_JSON}" \
        -o "connector/utility-grdf" --enable-post-process-file \
        --additional-properties=packageName=grdf_client,packageVersion=1.0.0,useInlineModelResolver=true,library=urllib3
