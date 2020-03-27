# -*- encode utf-8 -*-

import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv, dotenv_values


basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(basedir, '.env')
load_dotenv(dotenv_path)

# Debug
DEBUG = os.environ.get("FLASK_DEBUG")
TESTING = os.environ.get("FLASK_TESTING")
DEVELOPMENT = os.environ.get("FLASK_DEVELOPMENT")

# Security
CSRF_ENABLED = os.environ.get("FLASK_CSRF_ENABLED")
CSRF_SESSION_KEY = os.environ.get("FLASK_SESSION_KEY")
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

# Database
SQLALCHEMY_DATABASE_URI = os.environ.get("FLASK_SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("FLASK_SQLALCHEMY_TRACK_MODIFICATIONS")
DATABASE_CONNECT_OPTIONS = os.environ.get("FLASK_DATABASE_CONNECT_OPTIONS")
