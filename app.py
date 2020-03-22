import logging
import multiprocessing as mp
import os
from pathlib import Path

import connexion
from flask import render_template

from commons.cache import cache
from commons.logging import setup_logging
from commons.mongodb import init_db
from commons.scheduler import scheduler, update_json

setup_logging()
logger = logging.getLogger('<module>')

FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', 5000)
UPDATE_AUTO = os.getenv('UPDATE_AUTO', 0)

logger.info(f'FLASK_RUN_HOST: {FLASK_RUN_HOST}')
logger.info(f'FLASK_RUN_PORT: {FLASK_RUN_PORT}')
logger.info(f'UPDATE_AUTO: {UPDATE_AUTO}')

app = connexion.App(__name__, specification_dir=Path('./specifications/'))

# Check if cache folder exists
cache_folder = Path('cache')
if not cache_folder.exists():
    cache_folder.mkdir()

cache.init_app(app.app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': Path('cache/'), 'CACHE_DEFAULT_TIMEOUT': 60,
                                'CACHE_THRESHOLD': 100})

app.add_api('swagger.yml')


@app.route('/')
@cache.cached(timeout=50)
def home():
    return render_template('home.html')


if __name__ == '__main__':
    # Force update of json files
    update_json()
    # Create DB with updated json (drop=True)
    init_db()
    # Start scheduler for future updates
    if UPDATE_AUTO:
        t = mp.Process(name='Update data', target=scheduler)
        t.start()
    app.run(host=FLASK_RUN_HOST, port=FLASK_RUN_PORT)
