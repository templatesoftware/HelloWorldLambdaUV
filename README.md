# 1. Overivew
* Use this package as a template to create a Python based AWS Lambda function using UV
* The lambda itself is very simple, intended to be cloned and then built upon, this package makes it easy to get 
  started to build, test, and deploy the application  
* This package uses [UV](https://docs.astral.sh/uv/) - a modern and  extremely fast Python package and project 
  manager 

#### 1.1 .Prerequisites
1. [Git installed](https://github.com/git-guides/install-git) on your computer
2. [Docker installed](https://docs.docker.com/engine/install/) on your computer
3. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and an AWS account 
4. [UV installed](https://docs.astral.sh/uv/getting-started/installation/) on your local computer

# 2. Building, deploying, and testing 
1. Clone this repo to your local computer via  <TK command>
2. Change directory into the cloned repo via ```cd <TK>``` 
3. Build the project with uv via ```uv build```
4. Run the unit tests with ``` uv run pytest```
5. If the package is building and the tests are running successfully you're ready to deploy the lambda to AWS!
   6. Alternatively, you can further test the package by following the steps in [Testing with Docker]
      (#Testing-with-Docker) 

## 2.1 Deploy to AWS
* You can deploy this lambda function to AWS via two different ways:
  1. **Zip file** - build and upload a zip file directly to the lambda console. This is simpler and faster. 
  2. **Dockerfile** - build a Lambda compatible docker image, upload it to ECR, then create your Lambda based on 
     that image. This is more complex than the zip file based approach - we recommend starting with option 1.

### 2.1.2 Deploy to AWS with a zip file:
1. We provide a ```zipFunction.sh``` to zip the dependencies and source code into a lambda compatible zip file. 
   Create the zip file by running ```sh zipFunction.sh```
2. After executing you should see a ```hello_world_uv_lambda.zip``` in the directory. This contains all the lambda 
   source code and its dependencies. We're now ready to upload this to S3 and create our function 
1. In the AWS console [create a new](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function) lambda function
   2. Select "Author from scratch"
   3. Enter a "Function Name" such as ```hello-world-uv-lambda```
   4. In Runtime, select ```Python 3.9```
   5. Use architecture ```x86_64```
   6. Click "create function"
![Console image](https://private-user-images.githubusercontent.com/188703309/389572918-a8741102-7f42-4886-8d90-636452f21ab1.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDU4MDcsIm5iZiI6MTczMjU0NTUwNywicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTcyOTE4LWE4NzQxMTAyLTdmNDItNDg4Ni04ZDkwLTYzNjQ1MmYyMWFiMS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDM4MjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iY2QyY2U1YTFjOWIzZGMyMGU5Y2EwZjhkNjRjZDE2OTFmNjM5NDAxODI5MjM5YTk3MWJlZjQwMDY3ZmI2MTZkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.R8wmJvSkOXQ357BPs2STlGYB0VMKPXcJlyYbS5djhkI)
7. You can now upload your zip file by selecting "Upload from" and selecting your newly created zip file
![zip file upload image](https://private-user-images.githubusercontent.com/188703309/389572905-0b14725f-1b32-4b61-93d6-d636ac321d98.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDU4MDcsIm5iZiI6MTczMjU0NTUwNywicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTcyOTA1LTBiMTQ3MjVmLTFiMzItNGI2MS05M2Q2LWQ2MzZhYzMyMWQ5OC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDM4MjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NTA2NWY0ZGY2ZDllMDhlZDBjMTcxYmFlZmNhOGUyZTc2NDNjODdlYzUxN2I0MTEyYjhkMzA4MzBhNWIzNGUxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aFL0lgKq_9m7cO8sWwungO0yplxyC4sTZ58dgp5W9_k)
8. Finally, update the "Runtime Settings" **Handler** to our handler ```src.hello_world_lambda_uv.lambda_handler.handler```
![change handler settings image](https://private-user-images.githubusercontent.com/188703309/389574331-0fe35ad7-1c56-4a1f-b1c3-5d8edef8cf9e.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDU5NDcsIm5iZiI6MTczMjU0NTY0NywicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTc0MzMxLTBmZTM1YWQ3LTFjNTYtNGExZi1iMWMzLTVkOGVkZWY4Y2Y5ZS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDQwNDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMWYwY2IxZmU1Y2NiYTNiNWUxMDA0Mzc3ZjExMDNmM2YyZmFjMjcwOTliNTFlNzI5MGQ0MDhkNGFhNDMwOWM0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.KqhPgOI5floedBPJeZVJy5KQtTTS78vY_KHImS0WZKE)
9. At this point you're ready to test your lambda, navigate to the "Test" section of the console, update the "Test 
   event" section to your name and hit "Test"
![testing in console image](https://private-user-images.githubusercontent.com/188703309/389580355-82602c34-8b0b-4aad-ab38-b16991779110.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI1NDY3MzYsIm5iZiI6MTczMjU0NjQzNiwicGF0aCI6Ii8xODg3MDMzMDkvMzg5NTgwMzU1LTgyNjAyYzM0LThiMGItNGFhZC1hYjM4LWIxNjk5MTc3OTExMC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEyNVQxNDUzNTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xMzk4YjRhNWUwYjExYzRjYTUzOTQyYWIxOWVmMGRmOGFiMzI0YWVlYmJiYmQzZDUyMTEzNzAwMWViYTYxNTZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.LE44xYz5mykPOnUxjFZvhQutW28Uyb72D_mlSnblhXQ)
10. Alternatively, you can test via the AWS CLI
```bash
aws lambda invoke \
    --function-name hello-world-uv-lambda \
    --cli-binary-format raw-in-base64-out \
    --payload '{ "name": "AJ Brown" }' \
    lambda_response.json
```
and the output will be written into ```lambda_response.json```:
```bash
cat lambda_response.json | jq
// output 
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\": \"Hello AJ Brown! From us-east-1.\"}"
}
```

### 2.1.3 Deploy to AWS with a Docker image:
1. 

## 2.2. Testing

### 2.2.1 Unit tests
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

### 2.2.3 Testing with Docker
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