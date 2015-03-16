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
            'squirrel-backend = squirrel.launcher.entrypoint:run',
            'squirrel-cli = squirrel.launcher.cli:run',
        ],
    },
}

setup(**setup_args)
