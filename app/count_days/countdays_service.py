from datetime import datetime

from flask_restx import abort


def get_count_days_between_dates(start_date_input, end_date_input, weekdays):
    dates = _validation_dates(start_date_input, end_date_input)
    weekdays = _validation_weekdays(weekdays)
    total_days = 0
    detail_days = [0, 0, 0, 0, 0, 0, 0]
    for day in weekdays:
        days_calculate = get_count_days_by_weekday(dates['start_date'], dates['end_date'], day)
        detail_days[day] = days_calculate
        total_days += days_calculate

    return {'total_days': total_days, 'detail_days': detail_days}


def get_count_days_by_weekday(start, end, weekday):
    num_weeks, remainder = divmod((end - start).days, 7)
    if (weekday - start.weekday()) % 7 <= remainder:
        return num_weeks + 1
    else:
        return num_weeks

def _validation_dates(start_date_input, end_date_input):
    start_date = datetime.strptime(start_date_input, '%d/%m/%Y')
    end_date = datetime.strptime(end_date_input, '%d/%m/%Y')

    if start_date > end_date:
        abort(400, 'The start date must be before the end date')

    return {'start_date': start_date, 'end_date': end_date}

def _validation_weekdays(weekdays):
    if len(weekdays) > 0:
        try:
            weekdays = list(map(int, weekdays))
        except:
            abort(400, 'Weekdays only access number between 0 and 6')
        for day in weekdays:
            if not isinstance(day, int) or day < 0 or day > 6:
                abort(400, 'Weekdays only access number between 0 and 6')
    return weekdays