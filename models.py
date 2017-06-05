# project/models.py


from views import db
import datetime


class History(db.Model):

    __tablename__ = "history"

    task_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    command = db.Column(db.String, nullable=False)
    launched_date = db.Column(db.Date, default=datetime.datetime.utcnow())

    def __init__(self, username, command, launched_date):
        self.username = username
        self.command = command
        self.launched_date = launched_date

    def __repr__(self):
        return '<username {0}>'.format(self.username)
