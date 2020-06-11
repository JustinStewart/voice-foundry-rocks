# Voice Foundry Rocks
This is an implementation of the "Going Serverless" exercise. It creates a serverless app that exposes parts of a simple Pet interface.

Development and deployment requires [Docker](https://docs.docker.com/get-docker/).

## Development
To run the service locally, use `docker-compose up --build`:
```bash
$ docker-compose up --build
$ wget http://localhost:8080/pets

[{
  "id": "d5592bdc-c4b2-48bd-a083-368664c36ea6"   
},
{
  "id": "4da5ed65-c3e2-4025-aa4a-3cdaac0540d0"
}]

$ wget http://localhost:8080/pets/d5592bdc-c4b2-48bd-a083-368664c36ea6

{
  "id": "d5592bdc-c4b2-48bd-a083-368664c36ea6",
  "name": "Penny",
  "genus": "Canis",
  "species": "familiaris",
  "variety": "Black Labrador Retriever",
  "temperament": "Wild"
}
```

## API Reference

### GET /pets

### POST /pets

### DELETE /pets/{petId}
