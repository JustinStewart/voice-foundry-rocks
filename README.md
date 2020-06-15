# Voice Foundry Rocks
This is an implementation of the "Going Serverless" exercise. It's my first Serverless application. To get creative and make it interesting, I made my Lambda a [Python WSGI app]() that serves up a simple HTTP Pet interface wrapping a DynamoDB table.

The deployment creates an S3 bucket, DynamoDB table, a Lambda function housing our WSGI app, and an API Gateway instance that handles routing. The plugin can then be used to seed our S3 files into DynamoDB through the API after the initial deployment. It also allows us to list the contents of the table after seeding.

## Development
To initialize the project:

```bash

```

You can spin up a local API and DynamoDB setup with the [docker-compose](https://docs.docker.com/get-docker/) command:

```bash
cd python-wsgi-app
docker-compose up --build
wget http://localhost:8080
```

## Deployment
To deploy the code
```bash
export AWS_PROFILE={YOUR_AWS_PROFILE}
cd voice-foundry-rocks
serverless deploy --aws-profile ${AWS_PROFILE}
serverless pets seed --aws-profile ${AWS_PROFILE}
# Serverless: Starting seeding process...
# Serverless: Adding Durant...
# Serverless: Adding Penny...
serverless pets list
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
