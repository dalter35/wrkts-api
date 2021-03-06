from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#dev db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wrkts'

#prod db
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

import api.views
import api.models
