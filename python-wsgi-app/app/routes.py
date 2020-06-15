from flask import abort, jsonify, request
from app.models import Pet


def create_pet():
    j = request.json
    pet = Pet.deserialize(j)
    pet.save()
    return jsonify(pet.dict()), 201


def list_pets():
    pets = Pet.list()
    return jsonify([pet.dict() for pet in pets])


def get_pet(pet_id: str):
    pet = Pet.get(pet_id)
    if not pet:
        abort(404, description="Pet not found")
    return jsonify(pet.dict())


def delete_pet(pet_id: str):
    pet = Pet.get(pet_id)
    if not pet:
        abort(404, description="Pet not found")
    pet.delete()
    return "", 204
