from commons.cache import cache
from commons.mongodb import get_db, get_date_query
from commons.utils import check_dates


# TODO Use a redis caching system

def read_all(startDate=None, endDate=None):
    result = cache.get(f'nation_{startDate}_{endDate}')
    if not result:
        start_date, end_date = check_dates(startDate, endDate)
        collection = get_db()['nation']
        query = get_date_query(start_date, end_date)
        result = [doc for doc in collection.find(query, {'_id': False})]
        cache.set(f'nation_{startDate}_{endDate}', result)
    return result
