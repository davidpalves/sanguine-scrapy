from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api

from api.common.commands import update_data_bp
from api.common.database import mongo, db

from api.resources.authentication import AuthenticationToken, UserDetail
from api.resources.blood_banks_list import BloodBanksList
from api.resources.blood_level_list import BloodLevelsList

app = Flask(__name__)
api = Api(app)
CORS(app)

app.register_blueprint(update_data_bp)

if app.config["ENV"] == "production":
    app.config.from_object('configurations.ProductionConfig')
else:
    app.config.from_object('configurations.DevelopmentConfig')

mongo.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)

api.add_resource(BloodLevelsList, '/')
api.add_resource(AuthenticationToken, '/auth-token/')
api.add_resource(BloodBanksList, '/bancos-cadastrados/')
api.add_resource(UserDetail, '/user/')