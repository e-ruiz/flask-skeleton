# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = False
DEVELOPMENT = False

CSRF_ENABLED = True
CSRF_SESSION_KEY = "*** YOUR SUPER SECRET KEY ***"
SECRET_KEY = "*** YOUR SUPER SECRET KEY ***"

# Database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@127.0.0.1:5432/api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}