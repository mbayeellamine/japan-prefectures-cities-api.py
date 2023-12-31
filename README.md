# japan-prefectures-cities-api-service

japan-prefectures-cities-api-service

## Screenshot
![Screenshot](./images/screenshot_.png)

```bash
# Clone the repository
git clone https://github.com/mbayeellamine/japan-prefectures-cities-api.py.git

# Change directory to the project folder
cd japan-prefectures-cities-api.py

# Build the Docker image
docker build -t japan-prefectures-cities-api-service .

# Run the Docker container
docker run -p 8000:8000 japan-prefectures-cities-api-service
```

## Assuming you have set up your AWS CLI and logged in
```
$(aws ecr get-login --no-include-email --region <your_aws_region>)
```

## Create an ECR repository
```
aws ecr create-repository --repository-name japan-prefectures-cities-api
```

## Build and tag the Docker image
```
docker build -t japan-prefectures-cities-api-service .
docker tag japan-prefectures-cities-api-service:latest <your_account_id>.dkr.ecr.<your_aws_region>.amazonaws.com/japan-prefectures-cities-api:latest
```

## Push the Docker image to ECR
```
docker push <your_account_id>.dkr.ecr.<your_aws_region>.amazonaws.com/japan-prefectures-cities-api:latest
```

## Create a Fargate task definition
```
aws ecs register-task-definition --family japan-prefectures-cities-api-task --network-mode awsvpc --requires-compatibilities FARGATE --cpu 256 --memory 512 --container-definitions '[{"name":"japan-prefectures-cities-api-container","image":"<your_account_id>.dkr.ecr.<your_aws_region>.amazonaws.com/japan-prefectures-cities-api:latest","cpu":256,"memory":512,"essential":true,"portMappings":[{"containerPort":8000,"hostPort":8000}]}]'
```

## Create a Fargate cluster (if not already created)
```
aws ecs create-cluster --cluster-name japan-prefectures-cities-cluster
```

## Run the Fargate task
```
aws ecs run-task --cluster japan-prefectures-cities-cluster --task-definition japan-prefectures-cities-api-task
```

# Deploy on AWS Lambda using Cli
```
aws lambda create-function \
  --function-name MyLambdaFunction \
  --runtime python3.10 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/execution_role \
  --handler main.handler \
  --zip-file fileb://function.zip


mkdir layer
pip install -r requirements.txt -t layer/python
cd layer
zip -r layer.zip .

aws lambda publish-layer-version \
  --layer-name FastApiLayer \
  --description "FastAPI layer" \
  --zip-file fileb://layer.zip

aws lambda update-function-configuration \
  --function-name YourFunctionName \
  --layers arn:aws:lambda:REGION:ACCOUNT_ID:layer:FastApiLayer:1

```