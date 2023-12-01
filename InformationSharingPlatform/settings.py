class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URL = ''


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfi(Config):
    DATABASE_URL = ''


class TestingConfig(Config):
    TESTING = True