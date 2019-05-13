"""App config."""
import os


class Config:
    """Global configuration variables."""

    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')

    # Assets
    LESS_BIN = os.environ.get('LESS_BIN')
    ASSETS_DEBUG = os.environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = os.environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = os.environ.get('TEMPLATES_FOLDER')
    COMPRESSOR_DEBUG = os.environ.get('COMPRESSOR_DEBUG')
