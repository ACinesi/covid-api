from datetime import datetime

import flask


def filter_by_dates(data, startDate, endDate):
    if not startDate and not endDate:
        return [item for item in data]

    start_date = None
    end_date = None
    if startDate:
        start_date = datetime.strptime(startDate, '%Y-%m-%d')
    if endDate:
        end_date = datetime.strptime(endDate, '%Y-%m-%d')

    if start_date and end_date:
        if end_date < start_date:
            return flask.make_response(flask.jsonify({'msg': 'startDate must be lower or equal than endDate'}), 401)

    filtered_data = data
    if start_date:
        filtered_data = [item for item in filtered_data if datetime.strptime(item['data'], '%Y-%m-%d %X') >=
                         start_date]
    if end_date:
        filtered_data = [item for item in filtered_data if datetime.strptime(item['data'], '%Y-%m-%d %X') <=
                         end_date]

    return filtered_data
