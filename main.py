from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
