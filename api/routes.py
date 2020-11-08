from api import app, mongo
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    niveis_sangue = mongo.db.niveis.find()

    output = []
    for nivel_sangue in niveis_sangue:
        output.append({
            'url': nivel_sangue['url'] or '', 
            'banco': nivel_sangue['banco'] or '',
            'data_extracao': nivel_sangue['data_extracao'] or '',
            'endereco': nivel_sangue['endereco'] or '',
            'cidade': nivel_sangue['cidade'] or '',
            'sangue': nivel_sangue['sangue'] or '',
        })

    return jsonify(output)

