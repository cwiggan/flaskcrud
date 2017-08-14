from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')
db = SQLAlchemy(app)
# Load the views
from app import views
from app import models