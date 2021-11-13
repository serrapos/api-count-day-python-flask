import unittest
from unittest import TestCase

import werkzeug
from werkzeug.exceptions import BadRequest

from app.count_days.countdays_service import _validation_dates, _validation_weekdays, get_count_days_between_dates


class TestCountDaysService(TestCase):

    def test_validation_dates(self):
        dates = _validation_dates('01/11/2021', '03/11/2021')
        self.assertEqual(dates['start_date'].strftime('%d/%m/%Y'), '01/11/2021')
        self.assertEqual(dates['end_date'].strftime('%d/%m/%Y'), '03/11/2021')

    def test_validation_dates_error_before(self):
        with self.assertRaises(BadRequest) as ctx:
            _validation_dates('03/11/2021', '01/11/2021')
        self.assertEqual("400 Bad Request: The browser (or proxy) sent a request that this server could not understand.", str(ctx.exception))

    def test_validation_dates_error_format_date(self):
        with self.assertRaises(ValueError) as ctx:
            _validation_dates('03/11/2021', 'NO DATE')
        self.assertEqual("time data 'NO DATE' does not match format '%d/%m/%Y'", str(ctx.exception))

    def test_validation_weekdays(self):
        self.assertTrue(_validation_weekdays([1, 2, 3]))

    def test_validation_weekdays_error_less(self):
        with self.assertRaises(BadRequest) as ctx:
            _validation_weekdays([-1])
        self.assertEqual("400 Bad Request: The browser (or proxy) sent a request that this server could not understand.", str(ctx.exception))

    def test_validation_weekdays_error_gretter(self):
        with self.assertRaises(BadRequest) as ctx:
            _validation_weekdays([7])
        self.assertEqual("400 Bad Request: The browser (or proxy) sent a request that this server could not understand.", str(ctx.exception))

    def test_validation_weekdays_error_format(self):
        with self.assertRaises(BadRequest) as ctx:
            _validation_weekdays(['a'])
        self.assertEqual("400 Bad Request: The browser (or proxy) sent a request that this server could not understand.", str(ctx.exception))

    def test_count_days(self):
        self.assertEqual(get_count_days_between_dates('01/11/2021', '30/11/2021', [0])['total_days'], 5)
        self.assertEqual(get_count_days_between_dates('01/11/2021', '30/11/2021', [0, 1, 2, 3, 4, 5, 6])['total_days'], 30)
        self.assertEqual(get_count_days_between_dates('01/11/2021', '30/11/2021', [2])['total_days'], 4)
        self.assertEqual(get_count_days_between_dates('01/01/2021', '31/12/2021', [0])['total_days'], 52)
        self.assertEqual(get_count_days_between_dates('01/01/2021', '31/12/2021', [0, 1, 2, 3, 4, 5, 6])['total_days'], 365)
        self.assertEqual(get_count_days_between_dates('01/01/2024', '31/12/2024', [0, 1, 2, 3, 4, 5, 6])['total_days'], 366)

        self.assertEqual(get_count_days_between_dates('01/01/2021', '31/12/2021', [0, 1, 2, 3, 4, 5, 6])['detail_days'],
                         [52, 52, 52, 52, 53, 52, 52])
