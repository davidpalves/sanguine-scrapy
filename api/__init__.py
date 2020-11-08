from flask import Flask
from flask_pymongo import PyMongo
from decouple import config

app = Flask(__name__)

MONGODB_SERVER = config('MONGODB_SERVER')
MONGODB_PORT = config('MONGODB_PORT')
MONGODB_DB = config('MONGODB_DB')

app.config["MONGO_URI"] = f"mongodb://{MONGODB_SERVER}:{MONGODB_PORT}/{MONGODB_DB}"

mongo = PyMongo(app)

from api import routes
