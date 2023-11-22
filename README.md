# Deploy HuggingFace Model on AWS Lambda

**Create a virtual environment with Python 3.11**

`python3.11 -m venv lambda-service`

**Activate the virtual environment**
- Windows:

  `lambda-service\Scripts\activate`

- macOS/Linux:

  `source lambda-service/bin/activate`

**Install the Dependencies**

`pip install -r requirements.txt`

**Set up the Project**

`mkdir lambda-service
cd lambda-service
mkdir lambda`

**Execute the following Python file**

`python download_model.py`

**Build the Docker Image**

`docker build -t analyzer:latest .`


**Run the Docker Image**

`docker run -p 9000:8080 analyzer:latest` 

**Invoke the Lambda Function Locally**

`curl -XPOST "http://localhost:9000/2022-11-22/functions/function/invocations" -d '{"text": "I love cold showers"}'`

**Creating the CDK Folder Schema**

`cd lambda-service 
mkdir cdk 
cd cdk`

**Initializing the CDK App**

`cdk init app --language typescript`

**Execute the following under the CDK folder**

`npm install -g aws-cdk
 npm install @aws-cdk/aws-apigatewayv2-alpha
 npm install @aws-cdk/aws-apigatewayv2-integrations-alpha`

 
**Configure AWS CLI**

`aws configure`


**Deploying with CDK** 

`cdk bootstrap` 

**Deploy the Stack**

`cdk deploy` 


**If baseencode64 error, then execute this command to decode the json** 
`curl -XPOST "https://your-api-endpoint.amazonaws.com/qa" -d '{"text": "I love API"}' -H "content-type: application/json"`












