from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

#defining the blueprint

    from flask import Blueprint
    main = Blueprint ('main', __name__)
    from . import views, error


