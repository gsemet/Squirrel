
from distutils.core import setup

version = "0.0.1"

setup_args = {
    'name': "Squirrel",
    'version': version,
    'entry_points': {
        'console_scripts': [
            'squirrel-backend = squirrel.launcher.entrypoint:run',
        ],
    },
}

setup(**setup_args)
