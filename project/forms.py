from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class AnsibleForm(FlaskForm):
    hostname = StringField(
        'hostname',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    playbook = SelectField(
        'playbook',
        choices=[
            ('bosh.yml', 'Bosh'), ('cloudfoundry.yml', 'Cloud Foundry'), ('redis.yml', 'Redis')
        ]
    )
    output_level = SelectField(
        'output_level',
        choices=[
            ('-v', '-v'), ('-vv', '-vv'), ('-vvv', '-vvv')
        ]
    )


class LoginForm(FlaskForm):
    name = StringField(
        'name',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired()]
    )


class AddUserForm(FlaskForm):
    name = StringField(
        'name',
        validators=[DataRequired()]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Length(min=6, max=35)]
    )
    password = PasswordField(
        'New Password', 
        validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')]
    )
    confirm = PasswordField(
        'Repeat Password'
    )
