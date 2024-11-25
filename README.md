# Overivew
* Use this package as a template to create a Python based AWS Lambda function using UV
* The lambda itself is very simple, intended to be cloned and then built upon, this package makes it easy to get 
  started to build, test, and deploy the application  
* This package uses [UV](https://docs.astral.sh/uv/) - a modern and  extremely fast Python package and project 
  manager 

#### Prerequisites
1. [Git installed](https://github.com/git-guides/install-git) on your computer
2. [Docker installed](https://docs.docker.com/engine/install/) on your computer
3. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and an AWS account 
4. [UV installed](https://docs.astral.sh/uv/getting-started/installation/) on your local computer

# Building, deploying, and testing 
1. Clone this repo to your local computer via  <TK command>
2. Change directory into the cloned repo via ```cd <TK>``` 
3. Build the project with uv via ```uv build```
4. Run the unit tests with ``` uv run pytest```
5. If the package is building and the tests are running successfully you're ready to deploy the lambda to AWS!
   6. Alternatively, you can further test the package by following the steps in [Testing with Docker]
      (#Testing-with-Docker) 

## Deploy to AWS
* You can deploy this lambda function to AWS via two different mechanisms:
  1. **Zip file** - build and upload a zip file directly to the lambda console. This is simpler and faster. 
  2. **Dockerfile** - build a Lambda compatible docker image, upload it to ECR, then create your Lambda based on 
     that image. This is more complex than the zip file based approach but makes your application more reproducible. 
     We recommend trying option 1 and moving onto the dockerfile based approach later 

### Deploy to AWS with a zip file:
1. We provide a ```zipFunction.sh``` to zip the dependencies and source code into a lambda compatible zip file. 
   Create the zip file by running ```sh ```
1. In the AWS console [create a new](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function) lambda function
   2. Select "Author from scratch"
   3. Enter a "Function Name" such as ```hello-world-uv-lambda```
   4. In Runtime, select ```Python 3.9```
   5. Use architecture ```x86_64```
   6. Click "create function"
7. You can now upload your zip file by selecting "Upload from" and selecting your newly created zip file 
8. 

### Deploy to AWS with a Docker image:
1. 

## Testing

### Unit tests
* To run the unit tests contained in ```tests/``` run ```uv run pytest```
```bash
~ uv run pytest             
===================================================== test session starts =====================================================
platform darwin -- Python 3.9.13, pytest-8.3.3, pluggy-1.5.0
rootdir: ..../Template/SmallTemplates/UVPythonCalculatorLambda/calculator-lambda-uv
configfile: pyproject.toml
testpaths: tests
collected 3 items                                                                                                             

tests/handler_test.py ...                                                                                               [100%]

====================================================== 3 passed in 0.07s ======================================================
```

### Testing with Docker
* Build your docker image ```docker build --provenance=false  --platform linux/arm64 -t hello-world-uv-lambda .``` 
  We name the image ```hello-world-uv-lambda```
* Once the image is built we can run it with:
  * ```
    docker run -e AWS_REGION=us-east-1 -v ~/.aws-lambda-rie:/aws-lambda -p 9002:8080 \                       
    --entrypoint /aws-lambda/aws-lambda-rie \
    docker-image:test \
    /usr/local/bin/python -m awslambdaric src/hello_world_lambda_uv/handler.handler
    ```


### Testing with AWS CLI 