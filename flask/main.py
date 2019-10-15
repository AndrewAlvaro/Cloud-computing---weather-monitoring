from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask_api import api, db
from flask_site import site
# from wsgi import main as app

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
basedir = os.path.abspath(os.path.dirname(__file__))

# # Update HOST and PASSWORD appropriately.
HOST = "35.232.83.178"
USER = "root"
PASSWORD = "root"
DATABASE = "users"
CONNECTION_NAME = "directed-strata-237809:us-central1:greenhouse"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
# app.config["SQLALCHEMY_DATABASE_URI"] = ('mysql+pymysql://{user}:{password}@{host}/{database}?unix_socket=/cloudsql/{connection_name}').format(user=USER, password=PASSWORD, host = HOST, database=DATABASE, connection_name=CONNECTION_NAME)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)

app.register_blueprint(api)
app.register_blueprint(site)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
