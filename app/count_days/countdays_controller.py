from flask_restx import Resource, reqparse, Namespace

from . import api_countdays

# Add namespace to API
countdays_api = Namespace('countdays')
api_countdays.add_namespace(countdays_api)

@api_countdays.route('/countdays')
class CountDaysController(Resource):

    @api_countdays.doc(responses={
        200: 'Respuesta correcta',
        400: 'Error en los datos recibidos'
    })
    @api_countdays.doc(params={'start_date': 'Fecha de inicio', 'end_date': 'Fecha de fin'})
    def get(self):
        """Calcula el numero de dias que hay entre 2 fechas"""
        parser = reqparse.RequestParser()
        parser.add_argument('start_date', type=str)
        parser.add_argument('end_date', type=str)
        args = parser.parse_args()
        start_date = args.get('start_date')
        end_date = args.get('end_date')
        return f'Contador de días entre: {start_date} y {end_date}'