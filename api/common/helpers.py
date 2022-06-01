from flask import jsonify
from flask_mail import Message

from api.common.utils import build_email_body

from run import execute_spiders

def force_data_update():
    message = 'All data was updated'
    try:
        execute_spiders()
    except Exception:
        message = 'Could not fetch data properly'
        return jsonify({'details': message}), 400
    return jsonify({'details': message}), 200

def notify_user_able_to_donate(user):
    from api.app import mail
    msg = Message("Precisamos de você!", sender="noreply@sanguine.org.br", recipients=[user.email])
    msg.body = build_email_body(recipient_name=user.nome)
    mail.send(msg)
