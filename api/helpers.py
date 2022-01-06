from flask import jsonify
from run import execute_spiders

def force_data_update():
    message = 'All data was updated'
    try:
        execute_spiders()
    except Exception:
        message = 'Could not fetch data properly'
        return jsonify({'details': message}), 400
    return jsonify({'details': message}), 200