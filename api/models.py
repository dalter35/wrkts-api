from api import app, db

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

# class Lifts(db.Model, CRUD, TimestampMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(120))

# class Runs(db.Model, CRUD, TimestampMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     terrain = db.Column(db.String(120))
#     distance = db.Column(db.Float)