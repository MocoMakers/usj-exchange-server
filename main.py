from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request
import json
import yaml
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)
import base64


import src.services.cloud_vision_service as vision_service
import src.services.description_prompt as prompt_service

db = SQLAlchemy()

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY']= config_data['settings']['app_key']
app.config['UPLOAD_FOLDER'] = config_data['settings']['upload_path']

from src.models import ItemPosting


@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.comww'})

@app.route('/TEST')
def test():
    return "hello"

@app.route('/image/description', methods = ['POST'])
def fetchDescription():
    if request.method == 'POST':
      posted_data = json.loads(request.data)
      image_string = request.files['image']
      image_name = posted_data['image_name']
      save_path = app.config['UPLOAD_FOLDER']+image_name

      with open(save_path, "wb") as fh:
            #saves files
            fh.write(base64.decodebytes(image_string))
      

      label_results = vision_service.detect_image_features(save_path)
      labelString = label_results['string_labels']

      description = prompt_service.description_prompt(labelString)

    # self,image,description, tags, status
      myItem = ItemPosting.ItemPosting(save_path, description, '', 'DRAFT', 1)

      db.session.add(myItem)

      output = {
          'image_id': 1234,
          'description': description
      }

      return json.dumps(output)


# initialize the app with the extension
db.init_app(app)