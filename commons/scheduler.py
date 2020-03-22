import logging
import os
import time
from pathlib import Path

import requests
import schedule

logger = logging.getLogger('<module>')

UPDATE_TIME = os.getenv('UPDATE_TIME', '00:00')
base_path = Path('static/data')

urls = {
    'dpc-covid19-ita-regioni.json':
        'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json',
    'dpc-covid19-ita-province.json':
        'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json',
    'dpc-covid19-ita-andamento-nazionale.json':
        'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json',
}


def update_json():
    for filename, url in urls.items():
        r = requests.get(url)
        with open(base_path/filename, 'wb') as f:
            f.write(r.content)
    logger.info('File json aggiornati.')


def scheduler():
    logger.info("Scheduler attivato.")
    logger.info(f'UPDATE_TIME: {UPDATE_TIME}')
    try:
        update_json()
        schedule.every().day.at(UPDATE_TIME).do(update_json)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.warning("Scheduler terminato.")
