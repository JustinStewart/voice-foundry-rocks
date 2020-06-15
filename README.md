# Voice Foundry Rocks
This is an implementation of the "Going Serverless" exercise. It's my first Serverless application. To get creative and make it interesting, I made my Lambda a [Python WSGI app](https://www.serverless.com/plugins/serverless-wsgi/) that serves up a simple HTTP Pet interface wrapping the DynamoDB table.

The deployment creates an S3 bucket, DynamoDB table, a Lambda function housing our WSGI app, and an API Gateway instance that handles routing. The plugin can then be used to seed our S3 files into DynamoDB through the API after the initial deployment. It also allows us to list the contents of the table after seeding.

![Image of Architecture](architecture.png)

## Development
To initialize the project:

```bash
git clone git@github.com:JustinStewart/voice-foundry-rocks.git
cd voice-foundry-rocks
npm install
```

You can spin up a local API and DynamoDB setup with the [docker-compose](https://docs.docker.com/get-docker/) command:

```bash
cd python-wsgi-app
docker-compose up --build
# dynamodb_1  | Initializing DynamoDB Local with the following configuration:
# dynamodb_1  | Port:	8000
# dynamodb_1  | InMemory:	true
# dynamodb_1  | DbPath:	null
# dynamodb_1  | SharedDb:	false
# dynamodb_1  | shouldDelayTransientStatuses:	false
# dynamodb_1  | CorsParams:	*
# dynamodb_1  |
# app_1       |  * Serving Flask app "app.wsgi" (lazy loading)
# app_1       |  * Environment: production
# app_1       |    WARNING: This is a development server. Do not use it in a production deployment.
# app_1       |    Use a production WSGI server instead.
# app_1       |  * Debug mode: off
# app_1       |  * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
# python-wsgi-app_init-db_1 exited with code 0
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:27] "POST /pets HTTP/1.1" 201 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "GET /pets/d648264a-79da-47f8-9006-cd02bdb9947f HTTP/1.1" 200 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "GET /pets HTTP/1.1" 200 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "DELETE /pets/d648264a-79da-47f8-9006-cd02bdb9947f HTTP/1.1" 204 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "GET /pets HTTP/1.1" 200 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "POST /pets HTTP/1.1" 201 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "POST /pets HTTP/1.1" 201 -
# app_1       | 172.27.0.5 - - [15/Jun/2020 14:57:28] "GET /pets HTTP/1.1" 200 -
# tests_1     | .
# tests_1     | ----------------------------------------------------------------------
# tests_1     | Ran 1 test in 10.283s
# tests_1     |
# tests_1     | OK
```

This brings up the service, DynamoDB, and runs tests against the API.

## Deployment
To deploy the code:

```bash
export AWS_PROFILE={YOUR_AWS_PROFILE}
cd voice-foundry-rocks
serverless deploy --aws-profile ${AWS_PROFILE}
# Serverless: Python executable not found for "runtime": python3.8
# Serverless: Using default Python executable: python
# Serverless: Packaging Python WSGI handler...
# Serverless: Packaging required Python packages...
# Serverless: Linking required Python packages...
# Serverless: Warning: Could not find werkzeug, please add it to your requirements.txt
# Serverless: Packaging service...
# Serverless: Excluding development dependencies...
# Serverless: Unlinking required Python packages...
# Serverless: Creating Stack...
# Serverless: Checking Stack create progress...
# ........
# Serverless: Stack create finished...
# Serverless: Uploading CloudFormation file to S3...
# Serverless: Uploading artifacts...
# Serverless: Uploading service voice-foundry-rocks.zip file to S3 (1.75 MB)...
# Serverless: Validating template...
# Serverless: Updating Stack...
# Serverless: Checking Stack update progress...
# .......................................
# Serverless: Stack update finished...
# Service Information
# service: voice-foundry-rocks
# stage: dev
# region: us-east-1
# stack: voice-foundry-rocks-dev
# resources: 14
# api keys:
#   None
# endpoints:
#   ANY - https://um8bqa8xwg.execute-api.us-east-1.amazonaws.com/dev
#   ANY - https://um8bqa8xwg.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
# functions:
#   app: voice-foundry-rocks-dev-app
# layers:
#   None
# Serverless: Run the "serverless" command to setup monitoring, troubleshooting and testing.

serverless pets seed --aws-profile ${AWS_PROFILE}
# Serverless: Starting seeding process...
# Serverless: Adding Durant...
# Serverless: Adding Penny...

serverless pets list --aws-profile ${AWS_PROFILE}
# Serverless: Listing...
# Serverless: [
#  {
#    "genus": "Canis",
#    "id": "f96cf7ef-f443-45d1-ac1a-1c5c07b2ef24",
#    "name": "Penny",
#    "species": "familiaris",
#    "temperament": "Wild",
#    "variety": "Black Labrador Retriever"
#  },
#  {
#    "genus": "Canis",
#    "id": "259bf15c-1adf-44bd-a883-c8c6052b358c",
#    "name": "Durant",
#    "species": "familiaris",
#    "temperament": "Meek",
#    "variety": "Maltese/Dachsund Mix"
#  }
#]
```
