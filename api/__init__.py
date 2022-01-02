from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object('configurations.ProductionConfig')
else:
    app.config.from_object('configurations.DevelopmentConfig')


mongo = PyMongo(app)

from api import routes
