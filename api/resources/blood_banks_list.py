from flask_restful import Resource, reqparse

from api.app import mongo
from api.common.utils import create_queryset_filters


def generate_response(filter):
    niveis_sangue = mongo.db.niveis

    output = []
    for nivel_sangue in niveis_sangue.find(filter):
        output.append({
            'url': nivel_sangue.get('url'),
            'banco': nivel_sangue.get('banco'),
            'endereco': nivel_sangue.get('endereco'),
            'cidade': nivel_sangue.get('cidade'),
            'estado': nivel_sangue.get('estado'),
            'unidade': nivel_sangue.get('unidade'),
        })
    
    return output

class BloodBanksList(Resource):
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('cidade', type=str, location='args')
        parser.add_argument('estado', type=str, location='args')
        parser.add_argument('banco', type=str, location='args')

        args = parser.parse_args()
        cidade = args['cidade']
        estado = args['estado']
        banco = args['banco']

        filter = create_queryset_filters(cidade=cidade, estado=estado, banco=banco)

        output = generate_response(filter=filter)

        return output