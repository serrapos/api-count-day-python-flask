from unittest import TestCase
from app import create_app

class TestCountDaysService(TestCase):

    def setUp(self):
        self.app = create_app()
        self.http = self.app.test_client()


    def test_countdays_ok(self):
        response = self.http.get(f'/api/countdays?start_date=01/11/2021&end_date=30/11/2021&weekdays=1')
        result = response.json
        self.assertEqual(200, response.status_code, response.data)
        self.assertEqual(result['total_days'], 5)

    def test_countdays_error(self):
        response = self.http.get(f'/api/countdays?start_date=01/11/2021&end_date=30/09/2021&weekdays=1')
        result = response.json
        self.assertEqual(400, response.status_code, response.data)

    def test_countdays_error_format(self):
        response = self.http.get(f'/api/countdays?start_date=01/11/2021&end_date=30/09/2021&weekdays=b')
        result = response.json
        self.assertEqual(400, response.status_code, response.data)