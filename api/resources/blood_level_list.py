import re
from flask_restful import Resource, reqparse
from api.app import mongo


class BloodLevelsList(Resource):
    def get(self):
        niveis_sangue = mongo.db.niveis

        parser = reqparse.RequestParser()

        parser.add_argument('cidade', type=str, location='args')
        parser.add_argument('estado', type=str, location='args')
        parser.add_argument('banco', type=str, location='args')

        args = parser.parse_args()
        cidade = args.get('cidade')
        estado = args.get('estado')
        banco = args.get('banco')

        filter = {}
        if cidade: filter['cidade'] = re.compile('^' + re.escape(cidade) + '$', re.IGNORECASE)
        if estado: filter['estado'] = re.compile('^' + re.escape(estado) + '$', re.IGNORECASE)
        if banco: filter['banco'] = re.compile('^' + re.escape(banco) + '$', re.IGNORECASE)

        output = []
        for nivel_sangue in niveis_sangue.find(filter):
            output.append({
                'url': nivel_sangue.get('url'),
                'banco': nivel_sangue.get('banco'),
                'data_extracao': str(nivel_sangue.get('data_extracao')),
                'endereco': nivel_sangue.get('endereco'),
                'cidade': nivel_sangue.get('cidade'),
                'estado': nivel_sangue.get('estado'),
                'unidade': nivel_sangue.get('unidade'),
                'sangue': nivel_sangue.get('sangue'),
            })
        
        return output