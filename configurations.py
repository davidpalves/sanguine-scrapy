from decouple import config


class Config(object):
    ENV = config('FLASK_ENV')
    
    MONGODB_SERVER = config('MONGODB_SERVER')
    MONGODB_PORT = config('MONGODB_PORT')
    MONGODB_DB = config('MONGODB_DB')

    POSTGRES_USER = config('POSTGRES_USER')
    POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
    POSTGRES_DB = config('POSTGRES_DB')
    POSTGRES_SERVER = config('POSTGRES_SERVER')

    MAIL_SERVER = config('MAIL_SERVER')
    MAIL_PORT = config('MAIL_PORT')

    SECRET_KEY = config('SECRET_KEY')

    MONGO_URI = f"mongodb://{MONGODB_SERVER}:{MONGODB_PORT}/{MONGODB_DB}"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
