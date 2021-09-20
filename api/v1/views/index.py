#!/usr/bin/python3
"""
view doct
"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Return json status code
    """
    return jsonify({"status": "OK"})
