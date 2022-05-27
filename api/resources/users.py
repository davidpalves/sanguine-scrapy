import re, hashlib
from flask_restful import fields, marshal_with, Resource, reqparse

from api.app import mongo
from api.common.utils import create_queryset_filters


def generate_response(filter):
    users = mongo.db.users

    output = []
    for user in users.find(filter):
        output.append({
            'nome': user.get('nome'),
            'cidade': user.get('cidade'),
        })
    
    return output

user_fields= {
    "nome": fields.String,
    "email": fields.String,
    "cidade": fields.String,
    "estado": fields.String,
    "genero": fields.String,
    "tipo_sanguineo": fields.String
}

class CreateUser(Resource):
    @marshal_with(user_fields)
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

        user_output = self.create_user(args)
        return user_output

    def create_user(self, args):
        users = mongo.db.users

        pwd = self.encrypt_password(args.senha)
        user = users.insert_one({ 
            "nome": args.nome,
            "email": args.email,
            "cidade": args.cidade,
            "estado": args.estado,
            "genero": args.genero,
            "tipo_sanguineo": args.tipo_sanguineo,
            "senha": pwd
        })

        return user

    def encrypt_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()