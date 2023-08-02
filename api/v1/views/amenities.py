#!/usr/bin/python3
"""Amenity objects that handles all default RESTFul API actions"""
from flask import abort, jsonify, request
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    data = [
        amenity.to_dict() for amenity in storage.all(Amenity).values()
    ]
    return jsonify(data)

@app_views.route('/amenities/<amenity_id>', method=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    res = storage.get(Amenity, amenity_id)
    if res is None:
        abort(404)
    return jsonify(res.to_dict())

@app_views.route('/amenities/<amenity_id>', method=['DELETE'],
                 STRICT_SLASHES=False)
def delete_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities', strict_slashes=False, method=['POST'])
def create_amenity():
    body = request.get_json()
    if type(body) != dict:
        return abort(400, {'message': 'Not a JSON'})
    if 'name' not in body:
        return abort(404, {'message': 'Missing name'})
    n_amenity = Amenity(**body)
    n_amenity.save
    return jsonify(n_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id0', strict_slashes=False, method=['PUT'])
def update_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    body = request.get_json()
    if type(body) != dict:
        return abort(400, {'message': 'not a JSON'})
    for k, v in body.items():
        if k not in ['id', 'created_at', 'update_at']:
            setattr(amenity, k, v)
    storage.save()
    return jsonify(amenity.to_dict()), 200