from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wrkts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

import api.views
import api.models


# if __name__ == '__main__':
#     app.run(debug=True)
