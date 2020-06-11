import boto3
import uuid
import voluptuous
from app import config

ddb = boto3.resource('dynamodb', endpoint_url=config.DDB_ENDPOINT_URL)
table = ddb.Table(config.DDB_TABLE)

_schema = voluptuous.Schema({
    voluptuous.Optional('id'): str,
    'name': str,
    'genus': str,
    'species': str,
    'variety': str,
    'temperament': str
})


class Pet:

    def __init__(self, *, id: str = None, name: str, genus: str, species: str, variety: str, temperament: str):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.genus = genus
        self.species = species
        self.variety = variety
        self.temperament = temperament

    def save(self):
        table.put_item(Item=self.dict())

    def delete(self):
        table.delete_item(Key={'id': self.id})

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genus': self.genus,
            'species': self.species,
            'variety': self.variety,
            'temperament': self.temperament
        }

    @classmethod
    def list(cls):
        response = table.scan()
        return [cls.deserialize(item) for item in response['Items']]

    @classmethod
    def get(cls, pet_id):
        response = table.get_item(Key={'id': pet_id})
        return cls.deserialize(response['Item'])

    @staticmethod
    def deserialize(d):
        return Pet(**_schema(d))
