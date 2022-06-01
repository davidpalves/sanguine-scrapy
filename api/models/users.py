from datetime import date, timedelta
from decouple import config
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
    data_nascimento = db.Column(db.Date())
    data_ultima_doacao = db.Column(db.Date())
    senha_hash = db.Column(db.String(128))

    def encrypt_password(self, password):
        self.senha_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.senha_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(config('SECRET_KEY'), expires_in=expiration)
        return s.dumps({'id': self.id})

    @property
    def age(self):
        age = 0
        today = date.today()
        birthdate = self.data_nascimento
        if birthdate:
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        return age

    @property
    def next_donation_date(self):
        last_donation = self.data_ultima_doacao
        if last_donation:
            return last_donation + timedelta(days=120)
        return date.today()

    @property
    def is_able_to_donate(self):
        able = False
        age = self.age
        today = date.today()

        if age >= 16 and age <= 69:
            if today >= self.next_donation_date:
                able = True

        return able

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config('SECRET_KEY'))
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