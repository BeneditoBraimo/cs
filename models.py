from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Occurrence(db.Model):
    __tablename__ = "occurrences"
    id = db.Column(db.Integer, primary_key=True)
    occurrence_type = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False, default="Pending")
    pass

class Recomendation(db.Model):
    pass

class Event(db.Model):
    pass

class Agent(db.Model):
    pass

class Location(db.Model):
    pass