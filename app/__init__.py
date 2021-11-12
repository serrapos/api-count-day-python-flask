from flask import Flask
from flask_restx import Api

from app.count_days import countdays_module


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(countdays_module, url_prefix='/api/countdays')

    return app
