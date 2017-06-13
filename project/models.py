# project/models.py


from views import db
import datetime


class History(db.Model):

    __tablename__ = "history"

    task_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    username = db.Column(db.String, nullable=False)
    hostname = db.Column(db.String, nullable=False)
    playbook = db.Column(db.String, nullable=False)
    output = db.Column(db.String, nullable=False)


    def __init__(self, date, username, hostname, playbook, output):
        self.date = date
        self.hostname = hostname
        self.username = username
        self.playbook = playbook
        self.output = output


    def __repr__(self):
        return '<username {0}>'.format(self.username)
