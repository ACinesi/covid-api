import flask
from handlers.utils import filter_by_dates
from commons.extensions import cache

# TODO Use a database storage
# TODO Use a redis caching system
# TODO Update file
with open('static/data/dpc-covid19-ita-andamento-nazionale.json') as f:
    data = flask.json.load(f)


def read_all(startDate=None, endDate=None):
    filtered_data = cache.get(f'nation_{startDate}_{endDate}')
    if not filtered_data:
        filtered_data = filter_by_dates(data, startDate, endDate)
        if filtered_data:
            cache.set(f'nation_{startDate}_{endDate}', filtered_data)
    return filtered_data
