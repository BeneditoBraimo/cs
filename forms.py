from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class OccurrenceForm(FlaskForm):
    occurrence_type = StringField('Occurrence type')
    occurrence_date = StringField('Occurrence data')
    description = StringField('Description')
    status = StringField('Status')