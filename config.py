"""Flask config class"""
import os


class Config:
    """Set Flask Configuration vars."""

    # General config
    TESTING = os.environ.get("TESTING")
    DEBUG = os.environ.get("DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME")


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')


class TestConfig(Config):
    DEBUG = False
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI')


