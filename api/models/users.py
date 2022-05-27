from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

from api.app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    nome = db.Column(db.String(120))
    cidade = db.Column(db.String(120))
    estado = db.Column(db.String(120))
    genero = db.Column(db.String(32))
    tipo_sanguineo = db.Column(db.String(32))
    senha_hash = db.Column(db.String(128))

    def encrypt_password(self, password):
        self.senha_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.senha_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer('secret_key', expires_in=600)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('secret_key')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

    def __repr__(self) -> str:
        return f'<User {self.email}>'