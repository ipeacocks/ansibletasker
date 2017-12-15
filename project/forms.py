from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, PasswordField, BooleanField
# from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class AnsibleForm(FlaskForm):
    ansible_user = StringField(
        'ansible_user',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
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
        validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=8, max=20)]
    )
    adminorno = BooleanField(
        'adminorno'
    )
