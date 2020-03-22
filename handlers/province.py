from commons.cache import cache
from commons.mongodb import get_date_query, get_db
from commons.utils import check_dates


# with open('static/data/dpc-covid19-ita-province.json') as f:
#     data = flask.json.load(f)


def read_all(startDate=None, endDate=None):
    result = cache.get(f'province_{startDate}_{endDate}')
    if not result:
        start_date, end_date = check_dates(startDate, endDate)
        collection = get_db()['province']
        query = get_date_query(start_date, end_date)
        result = [doc for doc in collection.find(query, {'_id': False})]
    cache.set(f'province_{startDate}_{endDate}', result)
    return result


def read_one(provinceName, startDate=None, endDate=None):
    result = cache.get(f'province_{provinceName}_{startDate}_{endDate}')
    if not result:
        start_date, end_date = check_dates(startDate, endDate)
        collection = get_db()['province']
        query = get_date_query(start_date, end_date)
        query['denominazione_provincia'] = provinceName
        result = [doc for doc in collection.find(query, {'_id': False})]
        cache.set(f'province_{provinceName}_{startDate}_{endDate}', result)
    return result
