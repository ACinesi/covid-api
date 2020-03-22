import logging
import os
from pathlib import Path

from flask import json
from pymongo import MongoClient, errors

from commons.utils import sanitize_date

logger = logging.getLogger('<module>')

basepath = Path('static/data')

collection_to_file = {
    'nation': 'dpc-covid19-ita-andamento-nazionale.json',
    'region': 'dpc-covid19-ita-regioni.json',
    'province': 'dpc-covid19-ita-province.json'
}

MONGO_INITDB_ROOT_USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'root')
MONGO_INITDB_ROOT_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'root')
MONGO_INITDB_HOST = os.getenv('MONGO_INITDB_HOST', '0.0.0.0')
MONGO_INITDB_PORT = os.getenv('MONGO_INITDB_PORT', '27017')
MONGO_INITDB_DATABASE = os.getenv('MONGO_INITDB_DATABASE', 'covid')
MONGO_INITDB_DROP_AT_STARTUP = os.getenv('MONGO_INITDB_DROP_AT_STARTUP', 0)

logger.info(f'MONGO_INITDB_DROP_AT_STARTUP: {MONGO_INITDB_DROP_AT_STARTUP}')
logger.info(f'MONGO_INITDB_DATABASE: {MONGO_INITDB_DATABASE}')

db = None


def init_db():
    try:
        client = MongoClient(
            host=[str(MONGO_INITDB_HOST) + ":" + str(MONGO_INITDB_PORT)],
            serverSelectionTimeoutMS=3000,
            username=MONGO_INITDB_ROOT_USERNAME,
            password=MONGO_INITDB_ROOT_PASSWORD,
        )

        logger.info(f'Server version: {client.server_info()["version"]}')
    except errors.ServerSelectionTimeoutError as err:
        logger.error(err)
        raise
    global db
    db = client[MONGO_INITDB_DATABASE]
    db_names = client.list_database_names()
    if MONGO_INITDB_DATABASE in db_names:
        logger.info(f'Database {MONGO_INITDB_DATABASE} already exist.')
        if not MONGO_INITDB_DROP_AT_STARTUP:
            return True
        else:
            client.drop_database(MONGO_INITDB_DATABASE)
            logger.info(f'Database {MONGO_INITDB_DATABASE} dropped before init (MONGO_INITDB_DROP_AT_STARTUP=0).')
    for collection_name, filename in collection_to_file.items():
        collection = db[collection_name]
        with open(basepath/filename, 'rb') as f:
            json_data = json.load(f)
        for el in json_data:
            el['data'] = sanitize_date(el['data'], as_date=True)
        collection.insert(json_data)
    return True


def get_db():
    global db
    return db


def get_date_query(start_date, end_date):
    query = {}
    if start_date and end_date:
        query = {"data": {"$gte": start_date, "$lte": end_date}}
    elif start_date:
        query = {"data": {"$gte": start_date}}
    elif end_date:
        query = {"data": {"$lte": end_date}}
    return query
