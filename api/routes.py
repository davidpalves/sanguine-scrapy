import re
from api import app, mongo
from flask import jsonify, request
import subprocess


@app.route('/', methods=['GET'])
@app.route('/v1/', methods=['GET'])
def index():
    niveis_sangue = mongo.db.niveis

    cidade = request.args.get('cidade')
    estado = request.args.get('estado')
    banco = request.args.get('banco')

    filter = {}
    if cidade: filter['cidade'] = re.compile('^' + re.escape(cidade) + '$', re.IGNORECASE)
    if estado: filter['estado'] = re.compile('^' + re.escape(estado) + '$', re.IGNORECASE)
    if banco: filter['banco'] = re.compile('^' + re.escape(banco) + '$', re.IGNORECASE)

    output = []
    for nivel_sangue in niveis_sangue.find(filter):
        output.append({
            'url': nivel_sangue.get('url'),
            'banco': nivel_sangue.get('banco'),
            'data_extracao': nivel_sangue.get('data_extracao'),
            'endereco': nivel_sangue.get('endereco'),
            'cidade': nivel_sangue.get('cidade'),
            'estado': nivel_sangue.get('estado'),
            'unidade': nivel_sangue.get('unidade'),
            'sangue': nivel_sangue.get('sangue'),
        })

    return jsonify(output), 200


@app.route('/fetch-data/')
def execute_script():
    script_command = './run.sh'
    message = 'All data was updated'
    try:
        subprocess.Popen(script_command, stdout=subprocess.PIPE)
    except Exception:
        message = 'Could not fetch data properly'
        return jsonify({'details': message}), 400
    return jsonify({'details': message}), 200
