from flask import Flask, jsonify
from app import routes

app = Flask(__name__)
app.add_url_rule(
    '/pets',
    'list-pets',
    routes.list_pets,
    methods=['GET']
)
app.add_url_rule(
    '/pets',
    'create-pet',
    routes.create_pet,
    methods=['POST']
)
app.add_url_rule(
    '/pets/<pet_id>',
    'get-pet',
    routes.get_pet,
    methods=['GET']
)
app.add_url_rule(
    '/pets/<pet_id>',
    'delete-pet',
    routes.delete_pet,
    methods=['DELETE']
)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
