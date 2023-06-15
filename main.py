from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request
import json
import yaml
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

db = SQLAlchemy()

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY']= config_data['settings']['app_key']

# initialize the app with the extension
db.init_app(app)

@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

@app.route('/image/description', methods = ['POST'])
def fetchDescription():
    if request.method == 'POST':
      posted_data = json.loads(request.data)
      image = posted_data['image']

      output = {
          'image_id': 1234,
          'description': "Yo dudes, get you diss productz"
      }

      return json.dumps(output)
    