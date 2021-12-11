import logging
import logging.config
import os
import sys

import yaml

config_path = os.path.join(sys.path[0], 'logger/logging.yaml')

with open(config_path, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    f.close()
