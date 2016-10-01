from api import app, db
from passlib.apps import custom_app_context as pwd_context

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
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __init__(self, email):
        self.email = email

    def as_dict(self):
        obj_d = {
            'email': self.email
        }
        return obj_d

class Workouts(db.Model, CRUD, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', backref=db.backref('workouts', lazy='dynamic'))

    def __init__(self, user):
        self.user = user

    def as_dict(self):
        obj_d = {
            'workout_id': self.id,
            'user_id': self.user_id
        }
        return obj_d

class Lifts(db.Model, CRUD, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120))
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    workout = db.relationship('Workouts', backref=db.backref('lifts', lazy='dynamic'))

    def __init__(self, workout, type):
        self.workout = workout
        self.type = type

    def as_dict(self):
        obj_d = {
            'workout_id': self.workout_id,
            'workout_type': self.type
        }
        return obj_d

class Runs(db.Model, CRUD, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    terrain = db.Column(db.String(120))
    distance = db.Column(db.Float)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    workout = db.relationship('Workouts', backref=db.backref('runs', lazy='dynamic'))

    def __init__(self, workout, terrain, distance):
        self.workout = workout
        self.terrain = terrain
        self.distance = distance

    def as_dict(self):
        obj_d = {
            'workout_id': self.workout_id,
            'run_terrain': self.terrain,
            'distance': self.distance
        }
        return obj_d


