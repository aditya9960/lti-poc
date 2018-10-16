
class Config(object):
    SECRET_KEY = "lti-flask-app-secret"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/students"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/students"


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}