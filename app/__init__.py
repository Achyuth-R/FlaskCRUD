import os
from flask import Flask

project_dir = os.path.dirname(os.path.abspath(__file__))
database_URI = "postgresql://ApplicationRole:applicationpassword@localhost:5432/Dev_DB"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from app.module.routes import *