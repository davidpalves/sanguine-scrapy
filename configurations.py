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
