from pathlib import Path
import multiprocessing as mp
import connexion
from flask import render_template

from commons.extensions import cache
from commons.scheduler import scheduler

# Create the application instance
app = connexion.App(__name__, specification_dir='./specifications/')
cache.init_app(app.app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': Path('cache/'), 'CACHE_DEFAULT_TIMEOUT': 60,
                                'CACHE_THRESHOLD': 100})

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# Create a URL route in our application for "/"
@app.route('/')
@cache.cached(timeout=50)
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    t = mp.Process(name='child procs', target=scheduler)
    t.start()
    app.run(host='0.0.0.0', port=5000, debug=True)
