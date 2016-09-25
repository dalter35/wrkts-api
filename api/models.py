from api import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class TimestampMixin(object):
    created = db.Column(db.DateTime, default=db.func.now())

class CRUD():   
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()   
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class Users(db.Model, CRUD, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def as_dict(self):
        obj_d = {
            'email': self.email
        }
        return obj_d