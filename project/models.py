# project/models.py


from main import db
import datetime


class History(db.Model):

    __tablename__ = "history"

    task_id = db.Column(db.Integer, primary_key=True)
    task_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    hostname = db.Column(db.String, nullable=False)
    playbook = db.Column(db.String, nullable=False)
    output = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, task_date, hostname, playbook, output, user_id):
        self.task_date = task_date
        self.hostname = hostname
        self.playbook = playbook
        self.output = output
        self.user_id = user_id

    def __repr__(self):
        return '<user_id {0}>'.format(self.user_id)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    history = db.relationship('History', backref='poster')
    role = db.Column(db.String, default='user')

    def __init__(self, create_date, name, email, password, role):
        self.create_date = create_date
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User {0}>'.format(self.name)
