FROM public.ecr.aws/docker/library/python:buster AS build-image

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

# Download the latest UV installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the UV installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the UV installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# working dir to source code
ARG FUNCTION_DIR="src/hello_world_lambda_uv/"

# Copy function code
RUN mkdir -p ${FUNCTION_DIR}

# Copy source code into FUNCTION_DIR
COPY src/* pyproject.toml  ${FUNCTION_DIR}

FROM build-image

# create vitrual env. for UV
RUN uv venv

# Install the function's dependencies into the function directory
RUN uv pip install -r ./${FUNCTION_DIR}/pyproject.toml --target ${FUNCTION_DIR}

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the built dependencies from the build-image
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

# Set the entrypoint to run the AWS Lambda runtime interface client
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]

# Specify handler
CMD [ "lambda_handler.handler" ]
