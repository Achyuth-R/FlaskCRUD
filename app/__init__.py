import os
from flask import Flask
from app.module import Config

project_dir = os.path.dirname(os.path.abspath(__file__))
# database_URI = "postgresql://ApplicationRole:applicationpassword@localhost:5432/Dev_DB"
database_URI = Config.DbConfig()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from app.module.routes import *