from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length


class AnsibleForm(FlaskForm):
    hostname = StringField(
        'hostname',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    textarea = TextAreaField(
        'textarea', render_kw={"rows": 4},
        validators=[DataRequired(), Length(max=140)]
    )
    playbook = SelectField(
    	'playbook',
        validators=[DataRequired()],
        choices=[
            ('bosh.yml', 'Bosh'), ('cloudfoundry.yml', 'Cloud Foundry'), ('redis.yml', 'Redis')
        ]
    )