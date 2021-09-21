#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.state import State
from models import storage
from flask import Flask, jsonify, abort
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False)
def lsStates():
    """
    Return a list with dict
    """
    lstates = []
    for key, value in storage.all('State').items():
        lstates.append(value.to_dic())
    return jsonify(lstates)


@app_views.route('/states/<state_id>', strict_slashes=False)
def return_obj_stateId(state_id):
    """
    function that return un obj with ID
    """
    obj_st = storage.get('State', state_id)
    if state_id is None:
        abort(404)
    return json.dump(obj_st.to_dict())
