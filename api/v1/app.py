#!/usr/bin/python3
"""Sets up the flask app"""

from flask import Flask
from os import getenv
from models import storage
from flask_cors import CORS
from api.v1.views import app_views


app = Flask(__name__)
CORS(app, resources=r'/*', origins=['0.0.0.0'])

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """teardown Closes the SQLAlchemy session"""
    return storage.close()

@app.errorpage
def error(e):
    """Handles 404 error page"""
    return jsonify({"error": "Not found"}), 404

if __name__ == 'main__':
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    host = ("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"