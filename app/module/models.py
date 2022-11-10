from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)

class TestTable(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)

def __init__(self, id, name):
    self.id = id
    self.name = name

def __repr__(self):
    return "<Name: {}>".format(self.name)