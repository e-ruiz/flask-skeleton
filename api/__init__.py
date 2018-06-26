# -*- coding: utf-8 -*-

# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define application object
api = Flask(__name__)

# Configurations
api.config.from_object('config')

# Define the database object which is imported
db = SQLAlchemy(api)

"""
# Error handling
@api.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
"""

# Import a module / component using its blueprint handler variable
from api.hello.controllers import hello

# Array com as rotas e os blueprints, #lazyDev
routes = [
    {'url': '/hello', 'blueprint': hello},
]

# Register blueprint(s) #lazyDev
for route in routes:
    api.register_blueprint(route['blueprint'], url_prefix=route['url'])
