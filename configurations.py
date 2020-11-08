from decouple import config


class Config(object):
    MONGODB_SERVER = config('MONGODB_SERVER')
    MONGODB_PORT = config('MONGODB_PORT')
    MONGODB_DB = config('MONGODB_DB')
    ENV = config('FLASK_ENV')

    MONGO_URI = f"mongodb://{MONGODB_SERVER}:{MONGODB_PORT}/{MONGODB_DB}"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
