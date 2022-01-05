from flask import jsonify
from run import execute_spiders
import subprocess

# def update_data():
#     script_command = 'python ../run.py'
#     message = 'All data was updated'
#     try:
#         subprocess.Popen(script_command, stdout=subprocess.PIPE)
#     except Exception:
#         message = 'Could not fetch data properly'
#         return jsonify({'details': message}), 400
#     return jsonify({'details': message}), 200

def force_data_update():
    message = 'All data was updated'
    try:
        test = execute_spiders()
        print(test)
    except Exception:
        message = 'Could not fetch data properly'
        return jsonify({'details': message}), 400
    return jsonify({'details': message}), 200