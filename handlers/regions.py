from commons.cache import cache
from commons.mongodb import get_date_query, get_db
from commons.utils import check_dates


def read_all(startDate=None, endDate=None):
    result = cache.get(f'region_{startDate}_{endDate}')
    if not result:
        start_date, end_date = check_dates(startDate, endDate)
        collection = get_db()['region']
        query = get_date_query(start_date, end_date)
        result = [doc for doc in collection.find(query, {'_id': False})]
        cache.set(f'region_{startDate}_{endDate}', result)
    return result


def read_one(regionName, startDate=None, endDate=None):
    result = cache.get(f'region_{regionName}_{startDate}_{endDate}')
    if not result:
        start_date, end_date = check_dates(startDate, endDate)
        collection = get_db()['region']
        query = get_date_query(start_date, end_date)
        query['denominazione_regione'] = regionName
        result = [doc for doc in collection.find(query, {'_id': False})]
        cache.set(f'region_{regionName}_{startDate}_{endDate}', result)
    return result
