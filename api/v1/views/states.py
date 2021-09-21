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


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deletestate(state_id=None):
    """Deletes a state"""
    del_stor = storage.get("State", state_id)
    if del_stor is None:
        abort(404)
    else:
        storage.delete(obj_st)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def createstate():
    """Create a state"""
    crt_st = request.get_json(silent=True)
    if crt_st is None:
        abort(400, "Not a JSON")
    elif "name" not in crt_st.keys():
        abort(400, "Missing name")
    else:
        new_s = state.State(**crt_st)
        storage.new(new_s)
        storage.save()
        return jsonify(new_s.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def updatestate(state_id=None):
    """Update a state"""
    obj = storage.get("State", state_id)
    if obj is None:
        abort(404)

    upst = request.get_json(silent=True)
    if upst is None:
        abort(400, "Not a JSON")
    else:
        for key, value in upst.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(obj, key, value)
        storage.save()
        resq = obj.to_dict()
        return jsonify(resq), 200
