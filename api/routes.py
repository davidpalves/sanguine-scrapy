from api import app, mongo
from flask import jsonify, Response
import subprocess


@app.route('/', methods=['GET'])
@app.route('/v1/', methods=['GET'])
def index():
    niveis_sangue = mongo.db.niveis

    output = []
    for nivel_sangue in niveis_sangue.find():
        output.append({
            'url': nivel_sangue['url'],
            'banco': nivel_sangue['banco'],
            'data_extracao': nivel_sangue['data_extracao'],
            'endereco': nivel_sangue['endereco'],
            'cidade': nivel_sangue['cidade'],
            'sangue': nivel_sangue['sangue'],
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
