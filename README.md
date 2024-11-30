# 1. Overview
* Use this package as a template to create a Python based AWS Lambda function using UV
* The lambda logic itself is very simple, intended to be cloned and then built upon, this package makes it easy to get 
  started to build, test, and deploy 
* This package uses [UV](https://docs.astral.sh/uv/) - a modern and  extremely fast Python package and project 
  manager

#### 1.1. Prerequisites
1. [Git](https://github.com/git-guides/install-git) 
2. [Docker](https://docs.docker.com/engine/install/)
3. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and an AWS account 
4. [UV](https://docs.astral.sh/uv/getting-started/installation/)
# 2. Building, deploying, and testing
## 2.1. Building
1. Download this repo to your local computer with:
    ```bash
    gh repo clone templatesoftware/HelloWorldLambdaUV
    ```
2. Change directory into the cloned repo:
    ``` bash
    cd HelloWorldLambdaUV
    ``` 
3. Build the project with uv:
    ```bash 
    uv build
    ```
4. Run the unit tests with
    ```bash 
    uv run pytest
    ```
5. If the build and tests run successfully, you're ready to deploy your Lambda to AWS.
   Alternatively, further test the package by following the steps in Testing with Docker.

## 2.2 Deploy to AWS
* You can deploy this lambda function to AWS in two different ways:
  1. **Zip file** - Build and upload a ZIP file directly to the Lambda console. This is simpler and faster. 
  2. **Dockerfile** - Build a Lambda-compatible Docker image, upload it to ECR, and then create your Lambda from that image. This method is more complex, so we recommend starting with option 1.

### 2.2.1 Deploy with a zip file:
1. Use the provided ```zipFunction.sh``` to package the dependencies and source code into a Lambda-compatible zip 
   file. 
    ```bash
    sh zipFunction.sh
    ```
2. After running the command, you should see a ```hello_world_uv_lambda.zip``` file in your directory. This file contains the Lambda source code and its dependencies, ready to be uploaded to S3.
3. In the AWS console [create a new lambda function](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function)
   1. Select **Author from scratch**
   2. Enter a "Function Name" e.g. ```hello-world-uv-lambda```
   3. Set the **Runtime** to ```Python 3.9```
   4. Choose **architecture** ```arm64```
   5. Click **Create function**
![Console image](https://private-user-images.githubusercontent.com/188703309/389572918-a8741102-7f42-4886-8d90-636452f21ab1.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDU4MDcsIm5iZiI6MTczMjU0NTUwNywicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTcyOTE4LWE4NzQxMTAyLTdmNDItNDg4Ni04ZDkwLTYzNjQ1MmYyMWFiMS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDM4MjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iY2QyY2U1YTFjOWIzZGMyMGU5Y2EwZjhkNjRjZDE2OTFmNjM5NDAxODI5MjM5YTk3MWJlZjQwMDY3ZmI2MTZkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.R8wmJvSkOXQ357BPs2STlGYB0VMKPXcJlyYbS5djhkI)
4. Once the function is created, upload the zip file by selecting **Upload from** and choosing the ```hello_world_uv_lambda.zip``` file
![zip file upload image](https://private-user-images.githubusercontent.com/188703309/389572905-0b14725f-1b32-4b61-93d6-d636ac321d98.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDU4MDcsIm5iZiI6MTczMjU0NTUwNywicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTcyOTA1LTBiMTQ3MjVmLTFiMzItNGI2MS05M2Q2LWQ2MzZhYzMyMWQ5OC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDM4MjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NTA2NWY0ZGY2ZDllMDhlZDBjMTcxYmFlZmNhOGUyZTc2NDNjODdlYzUxN2I0MTEyYjhkMzA4MzBhNWIzNGUxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aFL0lgKq_9m7cO8sWwungO0yplxyC4sTZ58dgp5W9_k)
5. Update the **Handler** setting to ```src.hello_world_lambda_uv.lambda_handler.handler```
![change handler settings image](https://private-user-images.githubusercontent.com/188703309/389574331-0fe35ad7-1c56-4a1f-b1c3-5d8edef8cf9e.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDU5NDcsIm5iZiI6MTczMjU0NTY0NywicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTc0MzMxLTBmZTM1YWQ3LTFjNTYtNGExZi1iMWMzLTVkOGVkZWY4Y2Y5ZS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDQwNDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMWYwY2IxZmU1Y2NiYTNiNWUxMDA0Mzc3ZjExMDNmM2YyZmFjMjcwOTliNTFlNzI5MGQ0MDhkNGFhNDMwOWM0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.KqhPgOI5floedBPJeZVJy5KQtTTS78vY_KHImS0WZKE)
6. You're now ready to test your deployed Lambda, navigate to [Testing your deployed lambda](#testing-your-deployed-lambda) to try it out


### 2.1.3 Deploy to AWS with a Docker image:
![badge](https://template-software-badges-storage-bucket.s3.us-east-1.amazonaws.com/badges/HelloWorldDockerTest/HelloWorldDockerTest-build.svg)

Utilizing a docker image to create lambda function is a great way to manage complex dependencies and ensure 
compatibility across different environments. However, it is slightly more complex than the zip file based approach: 
1. build the Docker image - this command tags our image with the name ```hello-world-lambda-uv```
    ```bash
    docker build --provenance=false  --platform linux/arm64 -t hello-world-lambda-uv .
    ```
2. In the AWS console, create a new **ECR** repository e.g. ```hello-world-lambda-uv```. This repository will be responsible for storing our Docker images.
3. Once the repository is created, open it and select **View push commands**
4. Follow the instructions to log into ECR using 
    ```bash
    aws ecr get-login-password...
    ```
   After executing you should see ```Login Succeeded``` 
5. Tag the local docker image
    ```bash 
    docker tag hello-world-lambda-uv:latest <your AWS account>.dkr.ecr.us-east-1.amazonaws.com/hellow-world-lambda-uv:latest
    ```
6. Push the Docker image to ECR (if you get a timeout or closed network connection retry the push command a few times):
    ```bash
    docker push <your aws account>.dkr.ecr.us-east-1.amazonaws.com/hello-world-lambda-uv:latest
    ```
7. Copy the URI from your unewly ploaded Docker image 
8. Navigate to the lambda console and [create a new function](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function)
   1. Select **Container image**
   2. Enter a **Function name** e.g. ```hello-world-lambda-uv-docker-image```
   3. Paste the ```uri``` from your uploaded Docker image and input it into **Container image URI**
   4. Choose *Architecture* ```x86_64```
   5. **Create function**
9. You're now ready to test your deployed Lambda, navigate to [Testing your deployed lambda](#testing-your-deployed-lambda) to try it out
 

## 2.3. Testing

### 2.3.1 Unit tests
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

### 2.3.2 Testing locally with Docker
* Build your docker image ```docker build --provenance=false  --platform linux/arm64 -t hello-world-uv-lambda .``` 
  We name the image ```hello-world-uv-lambda```
* Once the image is built we can run it with:
```bash
docker run -e AWS_REGION=us-east-1 \
  -v ~/.aws-lambda-rie:/aws-lambda \
  -p 9002:8080 \
  --entrypoint /aws-lambda/aws-lambda-rie \
  hello-world-lambda-uv \
  /usr/local/bin/python -m awslambdaric lambda_handler.handler

```

* While that's running on port ```9002``` - open a seperate terminal window and send a request:
```bash
curl "http://localhost:9002/2015-03-31/functions/function/invocations" -d '{"name": "John Smith"}'   | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   154  100   132  100    22  14230   2371 --:--:-- --:--:-- --:--:-- 17111
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\": \"Hello John Smith! From us-east-1.\"}"
}
```


### 2.3.3 Testing your deployed lambda 

#### Testing in the console

1. In your lambdas AWS console, navigate to the **Test** section 
2. Update the **Test event** section to your name and hit **Test** - the response should be a ```200``` code with a ```Hello...```
    mesage in the body  
    ![testing in console image](https://private-user-images.githubusercontent.com/188703309/389580355-82602c34-8b0b-4aad-ab38-b16991779110.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDY3MzYsIm5iZiI6MTczMjU0NjQzNiwicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTgwMzU1LTgyNjAyYzM0LThiMGItNGFhZC1hYjM4LWIxNjk5MTc3OTExMC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDUzNTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xMzk4YjRhNWUwYjExYzRjYTUzOTQyYWIxOWVmMGRmOGFiMzI0YWVlYmJiYmQzZDUyMTEzNzAwMWViYTYxNTZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.LE44xYz5mykPOnUxjFZvhQutW28Uyb72D_mlSnblhXQ)
   ```json
   {
    "name": "Joe Smith"
   }
   ```


#### Testing with the CLI 

Alternatively, you can test via the AWS CLI:
1. Execute this lambda-invoke command from your terminal:
   ```bash
   aws lambda invoke \
      --function-name hello-world-uv-lambda \
      --cli-binary-format raw-in-base64-out \
      --payload '{ "name": "AJ Brown" }' \
      lambda_response.json
   ```
2. the response from the lambda will be written into ```lambda_response.json```:
   ```bash
   cat lambda_response.json | jq
   ```
   Output:
   ```json 
   {
     "statusCode": 200,
     "headers": {
       "Content-Type": "application/json"
     },
     "body": "{\"message\": \"Hello AJ Brown! From us-east-1.\"}"
   }
   ```