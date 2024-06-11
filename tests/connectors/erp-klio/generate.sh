#!/bin/bash
# ----------------------------------------------------------------------------------------------
# Generate the client code for the ERP-Klio connector from the OpenAPI 3.0 specification
# ----------------------------------------------------------------------------------------------
# May need to run once from the UI (will fail) to update the .cache
export PYTHON_POST_PROCESS_FILE="/usr/bin/yapf3 -i "

SCRIPT_DIR=$(dirname "$0")
PROJECT_DIR="${SCRIPT_DIR}/../../.."
cd "${PROJECT_DIR}" || exit

OPEN_API_JSON=$(python3 core/utils.py dereference "./connector/erp-klio-openapi.json")

JAVA=/snap/pycharm-professional/387/jbr/bin/java
#JAVA=java

${JAVA} --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED \
  -jar /home/jm/.cache/JetBrains/PyCharm2024.1/openapi/codegen/71aab8d6724718f581fedb5bf4fd5866/openapi-generator-cli-6.2.0.jar generate \
  -g python \
  -i "${OPEN_API_JSON}" \
  -o "tests/connectors/erp-klio" \
  --additional-properties=packageName=erp_klio_client,packageVersion=1.0.0,useInlineModelResolver=false,library=urllib3

# Automated improvements of docs
cd "${SCRIPT_DIR}"/docs || exit

# Function to process markdown files in a directory
process_files() {
    for file in *.md; do
        echo "Processing $file"
        python3 "${PROJECT_DIR}/core/utils.py" format_md "$file"
    done
}

# Process files in "apis" directory
echo "Postprocessing APIs..."

for tag in apis/*; do
  pushd "${tag}"
  process_files
  popd
done

# Navigate back to "docs" and then into "models"
cd models
echo "Postprocessing Models..."
process_files

echo "Postprocessing complete."
