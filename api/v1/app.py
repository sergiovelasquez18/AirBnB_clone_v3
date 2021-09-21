#!/usr/bin/python3
"""
Create API
"""
from flask import Flask, make_response
from flask.json import jsonify
from models import storage
from os import getenv
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(error):
    """
    function that close the section web
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    """error handling, 404"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=getenv(
            'HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', 5000),
            debug=True, threaded=True)
