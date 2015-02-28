========
Squirrel
========

Asset Portfolio Management System.


Installation
============

Installation is done using the scripts located in the ``install`` directory.

Squirrel runs its own virtuelenv, to avoid

Prerequisits
************

Have python 2.7, pip and virtualenv installed on your system::

    $ python
    $ pip
    $ pip install virtualenv

Windows
*******

``python.exe`` and ``virtualenv.exe`` should be accessible through your path.

Backend
-------

Please ensure you have pywin32 installed:

Choose in the `Pywin32 website`_ the version matching your version of python (2.7, 3.4, ...) and 32
or 64 bits.

.. _Pywin32 website: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

Windows virtualenv uses ``--system-site-packages`` to access to the ``win32api`` module.

Installation::

    python.exe -u install\\squirrel-install.py


Launching unit tests (from outside of virtualenv)::

    install\\unittest.bat squirrel


Building documentation::

    cd doc
    make.bat html

Fontend
-------

Please ensure you have the following tools installed:

- npm
- yeoman (only used to generate the gulp file)  (``npm instal -g yo``)
- bower (``npm install -g bower``)
- gulp (``npm install -g gulp``)
- Gulp Angular Generator for Yeoman (``npm install -g generator-gulp-angular``)

Linux
*****

Installation::

    python install/install.py

Switch to environment (activate virtualenv)::

    source tosource

Leave virtualenv::

    deactivate

Clean Virtualenv::

    python install/uninstall.py

Development
***********

Basically, you just need to run ``install/install.py`` and let all the magic happen. Everything
will be automatically regenerated:

- frontend (Web UI using Angular)
- backend (Python based)
- online documentation (using sphinx)

Frontend
--------

Gulp file (re)generation::

    cd frontend
    yo gulp-angular squirrel

See `generator-gulp-angular`_

.. _generator-gulp-angular: https://github.com/Swiip/generator-gulp-angular

Development:

- ``gulp`` or ``gulp build`` to build an optimized version of your application in /dist
- ``gulp serve`` to launch a browser sync server on your source files
- ``gulp serve:dist`` to launch a server on your optimized application
- ``gulp test`` to launch your unit tests with Karma
- ``gulp test``:auto to launch your unit tests with Karma in watch mode
- ``gulp protractor`` to launch your e2e tests with Protractor
- ``gulp protractor``:dist to launch your e2e tests with Protractor on the dist files

Editor configuration
--------------------

I use `SublimeText 3`_  as my main development environment. Here are the custom build command I
have used in this project::

    "build_systems":
    [
        {
            "name": "Squirrel - Install and launch",
            "cmd": ["python", "-u", "install\\install.py"],
            "shell": true,
            "working_dir": "X:\\Full\\Path\\Where\\Is\\Installed\\Squirrel"
        },
        {
            "name": "Squirrel - Unit test",
            "cmd": ["install\\unittest.bat", "squirrel"],
            "shell": true,
            "working_dir": "X:\\Full\\Path\\Where\\Is\\Installed\\Squirrel"
        },
        {
            "name": "Squirrel - Build documentation",
            "cmd": ["make.bat", "html"],
            "shell": true,
            "working_dir": "X:\\Full\\Path\\Where\\Is\\Installed\\Squirrel\\doc"
        },
        {
            "name": "Squirrel - Build Frontend",
            "cmd": ["gulp", "build"],
            "shell": true,
            "working_dir": "X:\\Full\\Path\\Where\\Is\\Installed\\Squirrel\\frontend"
        }
    ]


.. _SublimeText 3: http://www.sublimetext.com/3
