from api import app
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from models import Users, Workouts, Lifts

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
		return user.as_dict(), 201

class WorkoutsAdd(Resource):
	def post(self):
		user = Users.query.filter_by(id=request.form['user_id']).first_or_404()
		print user.email + ' added a workout'
		workout = Workouts(user)
		workout.add(workout)
		
		lift_type = request.form['lift_type']
		lift = Lifts(workout, lift_type)
		lift.add(lift)
		return lift.as_dict(), 201

		
api.add_resource(UsersList, '/users')
api.add_resource(WorkoutsAdd, '/workouts')