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

@app.route("/report_occurrence", methods=["POST"])
def report_occurence(request):
    pass