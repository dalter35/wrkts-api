from api import app
from flask import request, g
from flask_restful import reqparse, abort, Api, Resource
from flask_httpauth import HTTPBasicAuth
from models import Users, Workouts, Lifts, Runs

api = Api(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = Users.query.filter_by(email = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

class UsersList(Resource):
	def get(self):
		users_query = Users.query.all()
		users = [user.as_dict() for user in users_query]
		return users
	def post(self):
		# print request.form['email']
		user_email = request.form['email']
		password = request.form['password']
		user = Users(user_email)
		user.hash_password(password)
		user.add(user)
		return user.as_dict(), 201

class AddRuns(Resource):
	decorators = [auth.login_required]

	def post(self):
		user = Users.query.filter_by(id=g.user.id).first_or_404()
		print user.email + ' added a run'
		
		workout = Workouts(user)
		workout.add(workout)

		run_terrain = request.form.get('terrain')
		run_distance = request.form.get('distance')
		run = Runs(workout, run_terrain, run_distance)
		run.add(run)

		return run.as_dict(), 201

class AddLifts(Resource):
	def post(self):
		user = Users.query.filter_by(id=request.form['user_id']).first_or_404()
		print user.email + ' added a lift'
		
		workout = Workouts(user)
		workout.add(workout)

		lift_type = request.form.get('lift_type')
		lift = Lifts(workout, lift_type)
		lift.add(lift)
		return lift.as_dict(), 201

class UserWorkouts(Resource):
	decorators = [auth.login_required]

	def get(self):
		workouts = Workouts.query.filter_by(user_id=g.user.id).all()
		return [workout.as_dict() for workout in workouts]

api.add_resource(UsersList, '/users')
api.add_resource(AddRuns, '/runs')
api.add_resource(AddLifts, '/lifts')
api.add_resource(UserWorkouts, '/workouts')