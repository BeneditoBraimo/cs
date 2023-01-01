from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from time import datetime
import config

app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Class models
class Occurrence(db.Model):
    __tablename__ = "occurrences"
    id = db.Column(db.Integer, primary_key=True)
    occurrence_type = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False, default="Pending")
    # establish relationship between the Occurrence model and the Agent model

class Recommendation(db.Model):
    __tablename__ = "recommendations"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    relevance = db.Column(db.String(), nullable=False)
    # establish relationship between the Recommendation model and the Agent model
    pass

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    starting_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    title = db.Column(db.String(), nullable=False)
    # establish relationship between Event model and the Location model
    pass

class Agent(db.Model):
    __tablename__ = "agents"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    pass

class Location(db.Model):
    pass