from flask import g
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse
from sqlalchemy import exc

from api.app import db
from api.models.users import User

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email_or_token, password):
    user = User.verify_auth_token(email_or_token)
    if not user:
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

class AuthenticationToken(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600}, 200