import re
from flask_restful import Resource, reqparse

from api.app import mongo


class BloodBanksList(Resource):
    def get(self):
        niveis_sangue = mongo.db.niveis

        parser = reqparse.RequestParser()

        parser.add_argument('cidade', type=str, location='args')
        parser.add_argument('estado', type=str, location='args')

        args = parser.parse_args()
        cidade = args['cidade']
        estado = args['estado']

        filter = {}
        if cidade: filter['cidade'] = re.compile('^' + re.escape(cidade) + '$', re.IGNORECASE)
        if estado: filter['estado'] = re.compile('^' + re.escape(estado) + '$', re.IGNORECASE)

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