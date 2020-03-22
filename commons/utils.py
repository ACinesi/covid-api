import re
from datetime import datetime

import flask


def check_dates(startDate, endDate):
    start_date = None
    end_date = None
    if startDate:
        start_date = datetime.strptime(startDate, '%Y-%m-%d')
    if endDate:
        end_date = datetime.strptime(endDate, '%Y-%m-%d')

    if start_date and end_date:
        if end_date < start_date:
            return flask.make_response(flask.jsonify({'msg': 'startDate must be lower or equal than endDate'}), 401)

    return start_date, endDate


def sanitize_date(date, pattern=r'^\d{4}-\d{2}-\d{2}', as_date=False):
    temp_date = re.search(pattern=pattern, string=date).group(0)
    if as_date:
        temp_date = datetime.strptime(temp_date, "%Y-%m-%d")
    return temp_date
