import os
basedir=os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'Not!!Hack22Me%9Please'
    SSL_DISABLE=False
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_RECORD_QUERIES=True


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URI') or 'sqlite:///'+os.path.join(basedir,'data_dev.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

    @classmethod
    def init_app(cls,app):
        Config.init_app(app)
        import  logging

        from logging.handlers import SMTPHandler
        credentials=None


config ={
    'development':DevelopmentConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}