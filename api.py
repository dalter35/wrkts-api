from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wrkts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api = Api(app)


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


class UsersList(Resource):
	def get(self):
		users_query = Users.query.all()
		users = [user.as_dict() for user in users_query]
		return users
	def post(self):
		# print request.form['email']
		user_email = request.form['email']
		user = Users(user_email)
		user.add(user)
		return request.form['email']
		

api.add_resource(UsersList, '/users')

if __name__ == '__main__':
    app.run(debug=True)
