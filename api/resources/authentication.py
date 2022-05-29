from flask import g
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse
from sqlalchemy import exc

from api.app import db
from api.models.users import User

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email_or_token, password):
    user = User.verify_auth_token(email_or_token)
    if not user:
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

class AuthenticationToken(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600}, 200


class UserDetail(Resource):
    @auth.login_required
    def get(self):
        user = g.user
        serialized_data = {
            "nome": user.nome,
            "email": user.email,
            "cidade": user.cidade,
            "estado": user.estado,
            "genero": user.genero,
            "tipo_sanguineo": user.tipo_sanguineo,
            "data_nascimento": str(user.data_nascimento),
            "data_ultima_doacao": str(user.data_ultima_doacao),
            "data_proxima_doacao": str(user.next_donation_date),
            "apto_a_doar": user.is_able_to_donate,
        }

        return {"data": serialized_data}, 200

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
