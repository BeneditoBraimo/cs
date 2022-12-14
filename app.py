from flask import request, render_template
from flask_migrate import Migrate
from flask_moment import Moment
from models import app, db
import config

moment = Moment(app)
app.config.from_object(config)

migrate = Migrate(app, db)


# endpoints

@app.route("/index")
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route("/show_report_form")
def show_report_form():
    title = "Ocurrence form"
    return render_template("occurrence.html", title=title)

@app.route("/occurrences/report_occurrence", methods=["POST"])
def report_occurrence():
    occurrence_type = request.form.get("occurrence_type")
    occurrence_date = request.form.get("occurrence_date")
    description = request.form.get("description")
    status = request.form.get("status")
    
    return render_template("index.html")