import os

HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', '8080')

S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
S3_BUCKET = os.getenv('S3_BUCKET', 'foo')

DDB_ENDPOINT_URL = os.getenv('DDB_ENDPOINT_URL')
DDB_TABLE = os.getenv('DDB_TABLE', 'bar')
