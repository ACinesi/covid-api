import logging
import logging.config
import os

import coloredlogs
import yaml


def setup_logging(default_path='config/logging.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                current_level = logging.getLogger().getEffectiveLevel()
                coloredlogs.install(level=current_level)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')
