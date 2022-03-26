from flask import Flask
from flask_restful import Api

from api.common.database import mongo
from api.common.commands import update_data_bp

from api.resources.blood_level_list import BloodLevelsList
from api.resources.blood_banks_list import BloodBanksList

app = Flask(__name__)
api = Api(app)

app.register_blueprint(update_data_bp)

if app.config["ENV"] == "production":
    app.config.from_object('configurations.ProductionConfig')
else:
    app.config.from_object('configurations.DevelopmentConfig')

mongo.init_app(app)

api.add_resource(BloodLevelsList, '/')
api.add_resource(BloodBanksList, '/bancos-cadastrados/')