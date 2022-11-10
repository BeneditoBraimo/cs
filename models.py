from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Occurrence(db.Model):
    pass

class Recomendation(db.Model):
    pass

class Event(db.Model):
    pass

class Agent(db.Model):
    pass

class Route(db.Model):
    pass