from api import app
from flask_restful import reqparse, abort, Api, Resource
from models import Users

api = Api(app)

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