# db_create.py

from main import db
from models import History, User
from datetime import date


db.create_all()
# login/pass - admin/admin
db.session.add(
    User(
        date(2016, 2, 23),
        'admin',
        'admin@example.com',
        '$2b$12$/6k5KPJ.BjICuNh8AyrQZeb9JlsgBt3p/LrWEha6pkvnYs9SBc9u.',
        'admin'
    )
)
db.session.commit()
