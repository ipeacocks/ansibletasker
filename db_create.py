# db_create.py


from views import db
from models import History
from datetime import date


# create the database and the db table
db.create_all()

# insert data
db.session.add(History("admin", 'ansible-playbook -i hosts bosh.yml', date(2015, 3, 13)))

# commit the changes
db.session.commit()