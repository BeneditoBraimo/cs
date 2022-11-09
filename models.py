from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)