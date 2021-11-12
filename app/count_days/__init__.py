from flask import Blueprint
from flask_restx import Api

countdays_module = Blueprint('countdays_module', __name__)
api_countdays = Api(countdays_module, version='1.0', title='Count Days API',
                    description='Contador de días entre dos fechas')

from . import countdays_controller