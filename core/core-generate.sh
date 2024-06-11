#!/bin/bash

LAMBDA_NAME="api_python_server"  # The main API server (written in Python)
SCRIPT_DIR="$(dirname "$0")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/..")"
cd "${PROJECT_DIR}" || exit 10

. "${PROJECT_DIR}/generate_functions.sh"

PACKAGE_NAME="api_python_server"
# Generate API files
generate_server_api 8081 /core/v1 ${PACKAGE_NAME}

# Add implementation file(s) to the API files
LAMBDA_NAME=core
APIS_DIR="${PROJECT_DIR}/core/api_${LAMBDA_NAME}_lambda/src/${PACKAGE_NAME}/apis"
(cd "${SCRIPT_DIR}" || exit 11 ; \
 ln -f "${LAMBDA_NAME}-implementation.py" "${APIS_DIR}/implementation.py")

# Automated code updates
# Loop over all APIs
for api in "clients" "data" "deprecated" "scenario" "time_ranges"; do
    finalize_api_file "${APIS_DIR}" "$api"
done

# Automated improvements of docs: if needed, see tests/connectors/erp-klio/generate.sh
