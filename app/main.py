import boto3
import click
from app import config
from app.models import ddb
from app.wsgi import app


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    client = boto3.client('dynamodb')
    try:
        ddb.create_table(
            TableName=config.DDB_TABLE,
            AttributeDefinitions=[{
                'AttributeName': 'id',
                'AttributeType': 'S'
            }],
            KeySchema=[{
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
    except client.exceptions.ResourceInUseException:
        click.echo("Table already exists...skipping.")


@cli.command()
def run():
    app.run(host=config.HOST, port=config.PORT)


if __name__ == '__main__':
    cli()
