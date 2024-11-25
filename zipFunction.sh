#!/bin/bash

ZIP_FILE_NAME="hello_world_uv_lambda.zip"

# make sure uv is installed
if command -v uv &> /dev/null; then
    echo "'uv' is installed."
else
    echo "'uv' is not installed. Please see the README for dirctions to install it before proceeding."
    exit 1
fi

# delete the zip file if its already been created
if [ -f "$ZIP_FILE_NAME" ]; then
  rm "$ZIP_FILE_NAME"
fi

# create a directory to install our dependencies into
mkdir -p lambda_upload_package

# make sure the directory is empty
rm -rf lambda_upload_package*
rm -rf /path/to/directory/.*

# install project dependencies into directory
uv pip install -r pyproject.toml --target lambda_upload_package

# zip up the dependency directory
zip -r "$ZIP_FILE_NAME" lambda_upload_package/

# put python source code into the zip file
zip -r "$ZIP_FILE_NAME" src/hello_world_lambda_uv/




