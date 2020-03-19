import flask

from commons.cache import cache
from commons.utils import filter_by_dates

with open('static/data/dpc-covid19-ita-province.json') as f:
    data = flask.json.load(f)


def read_all(startDate=None, endDate=None):
    filtered_data = cache.get(f'province_{startDate}_{endDate}')
    if not filtered_data:
        filtered_data = filter_by_dates(data, startDate, endDate)
        if filtered_data:
            cache.set(f'province_{startDate}_{endDate}', filtered_data)
    return filtered_data


def read_one(provinceName, startDate=None, endDate=None):
    filtered_data = cache.get(f'province_{provinceName}_{startDate}_{endDate}')
    if not filtered_data:
        filtered_data = [item for item in data if str.lower(item['denominazione_provincia']) == str.lower(provinceName)]
        if filtered_data:
            filtered_data = filter_by_dates(filtered_data, startDate, endDate)
            if filtered_data:
                cache.set(f'province_{provinceName}_{startDate}_{endDate}', filtered_data)
    return filtered_data
