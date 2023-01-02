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
class Agent(db.Model):
    __tablename__ = "agents"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    occurrences = db.relationship(
        "Agent", backref="occurrences", lazy=True, cascade="all, delete-orphan"
    )
    recommendations = db.relationship(
        "Agent", backref="recommendations", lazy=True, cascade="all, delete-orphan"
    )
    
class Province(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    locations = db.relationship(
        "Province", backref="locations", lazy=True, cascade="all, delete-orphan"
    )
class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey(Province.id))
    events = db.relationship(
        "Location", backref="events", lazy=True, cascade="all, delete-orphan"
    )

    occurrences = db.relationship(
        "Location", backref="occurences", lazy=True, cascade="all, delete-orphan"
    )



class Occurrence(db.Model):
    __tablename__ = "occurrences"
    id = db.Column(db.Integer, primary_key=True)
    occurrence_type = db.Column(db.String(), nullable=False)
    occurence_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    description = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False, default="Pending")
    agent_id = db.Column(db.Integer, db.ForeignKey(Agent.id))
    location_id = db.Column(db.Integer, db.ForeignKey(Location.id))

class Recommendation(db.Model):
    __tablename__ = "recommendations"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    relevance = db.Column(db.String(), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey(Agent.id))

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    starting_date = db.Column(db.DateTime(timezone=True), nullable=False)
    title = db.Column(db.String(), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey(Location.id))
