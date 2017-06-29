# project/models.py


from views import db
import datetime


class History(db.Model):

    __tablename__ = "history"

    task_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    hostname = db.Column(db.String, nullable=False)
    playbook = db.Column(db.String, nullable=False)
    output = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date, hostname, playbook, output, user_id):
        self.date = date
        self.hostname = hostname
        self.playbook = playbook
        self.output = output
        self.user_id = user_id

    def __repr__(self):
        return '<user_id {0}>'.format(self.user_id)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    history = db.relationship('History', backref='poster')

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User {0}>'.format(self.name)
