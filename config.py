import secrets


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123456@localhost/covdb_dev'
    SECRET_KEY = secrets.token_urlsafe(16)
    UPLOAD_FOLDER = 'application/uploads/forms'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx','odt'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root123456@localhost/covdb'
    SECRET_KEY = secrets.token_urlsafe(16)
    UPLOAD_FOLDER = 'application/uploads/forms'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx', 'odt'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
