import flask

from handlers.utils import filter_by_dates
from commons.extensions import cache

with open('static/data/dpc-covid19-ita-regioni.json') as f:
    data = flask.json.load(f)


def read_all(startDate=None, endDate=None):
    filtered_data = cache.get(f'region_{startDate}_{endDate}')
    if not filtered_data:
        filtered_data = filter_by_dates(data, startDate, endDate)
        if filtered_data:
            cache.set(f'region_{startDate}_{endDate}', filtered_data)
    return filtered_data


def read_one(regionName, startDate=None, endDate=None):
    filtered_data = cache.get(f'region_{regionName}_{startDate}_{endDate}')
    if not filtered_data:
        filtered_data = [item for item in data if item['denominazione_regione'] == regionName]
        if filtered_data:
            filtered_data = filter_by_dates(filtered_data, startDate, endDate)
            if filtered_data:
                cache.set(f'region_{regionName}_{startDate}_{endDate}', filtered_data)
    return filtered_data
