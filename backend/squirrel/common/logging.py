from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import logging.config as logging_config

from squirrel.config.load_config import Config


log = logging.getLogger(__name__)


def setupLogger():
    logging_config.fileConfig(Config().frontend.logging_conf_full_path)
    logging.debug("Logger configured by: {}".format(Config().frontend.logging_conf_full_path))
