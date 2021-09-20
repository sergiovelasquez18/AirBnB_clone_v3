#!/usr/bin/python3
"""
Create API
"""
from flask import Flask
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close():
    """
    function that close the section web
    """
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv(
        'HBNB_API_HOST, '0.0.0.0'), port=getenv(
            'HBNB_API_PORT', '5000'),
            debug=True,
            threaded=True)
