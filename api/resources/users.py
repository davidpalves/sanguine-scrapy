from flask_restful import Resource, reqparse
from sqlalchemy import exc

from api.app import db
from api.models.users import User

class CreateUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("nome", dest="nome", required=True)
        parser.add_argument("email", dest="email", required=True)
        parser.add_argument("cidade", dest="cidade", required=True)
        parser.add_argument("estado", dest="estado", required=True)
        parser.add_argument("genero", dest="genero", required=True)
        parser.add_argument("tipo_sanguineo", dest="tipo_sanguineo", required=True)
        parser.add_argument("senha", dest="senha", required=True)
        
        args=parser.parse_args()

        response = self.create_user(args)
        
        return response

    def create_user(self, args):
        raw_password = args.pop("senha")
        
        user = User(**args)

        args["senha_hash"] = user.encrypt_password(raw_password)
        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return {'message': 'This email is already being used.'}, 400

        return {'message': 'User successfully registered'}, 201
