from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class AnsibleForm(FlaskForm):
    hostname = StringField(
        'hostname',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    textarea = StringField(
        'textarea',
        validators=[DataRequired(), Length(min=6, max=40)]
    )
