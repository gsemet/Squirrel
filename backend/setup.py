from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from distutils.core import setup

version = "0.0.1"

setup_args = {
    'name': "Squirrel",
    'version': version,
    'entry_points': {
        'console_scripts': [
            'squirrel-heroku = squirrel.launcher.heroku_server:run',
            'squirrel-prod = squirrel.launcher.squirrel_prod:run',
            'squirrel-dev = squirrel.launcher.squirrel_dev:run',
            'squirrel-cli = squirrel.launcher.squirrel_cli:run',
            'auto_relauncher = squirrel.launcher.auto_relauncher:run',
        ],
    },
}

setup(**setup_args)
