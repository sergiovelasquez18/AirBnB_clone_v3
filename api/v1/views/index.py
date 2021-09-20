#!/usr/bin/python3
"""
view doct
"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify


@app_view.route('/status')
def status():
    """
    Return json status code
    """
    return jsonify({"status": "OK"})
