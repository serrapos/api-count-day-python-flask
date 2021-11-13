from flask_restx import fields

from app.count_days import api_countdays

countdays_response = api_countdays.model('CountDaysModel', {
    'total_days': fields.Integer(required=True, description='Number of days between start_date and end_date'),
    'detail_days': fields.Integer(required=True, description='Number of days between start_date and end_date per weekday')
})