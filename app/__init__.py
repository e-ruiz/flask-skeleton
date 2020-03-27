# -*- coding: utf-8 -*-

# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define application object
app = Flask(__name__)

# Configurations
app.config.from_object('settings')

# Define the database object which is imported
db = SQLAlchemy(app)

"""
# Error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
"""

# Import a module / component using its blueprint handler variable
from app.hello.controllers import hello

# Array com as rotas e os blueprints, #lazyDev
routes = [
    {'url': '/hello', 'blueprint': hello},
]

# Register blueprint(s) #lazyDev
for route in routes:
    app.register_blueprint(route['blueprint'], url_prefix=route['url'])


