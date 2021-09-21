#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.amenities import Amenity
from models import storage
from flask import Flask, jsonify, abort
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False)
def lsAmenity():
    """

    """
    lAmenity = []
    for key, value in storage.all('Amenity').items():
        lAmenity.append(value.to_dic())
    return jsonify(lAmenity)


@app_views.route('/states/<amenity_id>', strict_slashes=False)
def return_obj_stateId(amenity_id):
    """
    function that return un obj with ID
    """
    obj_st = storage.get('Amenity', amenity_id)
    if amenity_id is None:
        abort(404)
    return json.dump(obj_st.to_dict())
