from flask import request
from flask_restx import Resource, reqparse, Namespace, abort

from app.count_days.schema import countdays_response
from . import api_countdays

# Add namespace to API
from .countdays_service import get_count_days_between_dates

countdays_api = Namespace('countdays')
api_countdays.add_namespace(countdays_api)

@api_countdays.route('')
class CountDaysController(Resource):

    @api_countdays.doc(responses={
        200: 'Respuesta correcta',
        400: 'Error en los datos recibidos'
    })
    @api_countdays.doc(params={'start_date': 'Fecha de inicio', 'end_date': 'Fecha de fin'})
    @api_countdays.marshal_with(countdays_response)
    def get(self):
        """Calcula el numero de dias que hay entre 2 fechas"""
        parser = reqparse.RequestParser()
        parser.add_argument('start_date', type=str)
        parser.add_argument('end_date', type=str)
        args = parser.parse_args()
        start_date = args.get('start_date')
        end_date = args.get('end_date')
        if start_date is None or end_date is None:
            abort(400, 'Los parámetros start_date y end_date son obligatorio')
        dict = request.args.to_dict(flat=False)
        weekdays = [] if not 'weekdays' in dict.keys() else dict['weekdays']
        return get_count_days_between_dates(start_date, end_date, weekdays)