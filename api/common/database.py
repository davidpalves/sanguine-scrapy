from flask_mail import Mail
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

db = SQLAlchemy()
mail = Mail()
mongo = PyMongo()
scheduler = APScheduler()
