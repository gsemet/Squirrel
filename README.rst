========
Squirrel
========

.. image:: https://img.shields.io/travis/Stibbons/Squirrel/master.svg
    :target: https://travis-ci.org/Stibbons/Squirrel

.. image:: https://img.shields.io/coveralls/Stibbons/Squirrel.svg
    :target: https://coveralls.io/r/Stibbons/Squirrel


Asset Portfolio Management System.


Installation
============

Installation is done using the ``install.py`` script located in the ``install`` directory.

Squirrel typically runs its own virtuelenv, to avoid conflict with installed Python libraries.

Prerequisits
************

Have python 2.7, pip and virtualenv installed on your system:

.. code-block:: bash

    $ python   # Python 2.7.9
    $ pip  # pip 6.0.8
    $ pip install virtualenv

To build the frontend UI (HTML), you'll need node, and bower. The build system uses ``gulp`` which
will be automatically installed by the Squirel Installer.

.. code-block:: bash

    $ npm install -g gulp
    $ npm install -g bower

Python 3
--------

Squirrel is not Python 3 compatible, the following dependencies needs to be ported first:

- Twisted

Targets
*******

Squirrel installation allows to select several type of installation targets:

``install:dev`` or ``serve:dev``

    Your prefered mode for hacking Squirrel. It will setup a virtualenv if ``workdir`` directory.
    ``isntall:dev`` only installs and do not start. ``serve:dev`` install and automatically start
    web server.

    It lauches the Python backend with autorestart (ie, as soon as you modify a python file, the
    backend is restarted), and starts the Angular frontend using ``gulp serve`` (ie, as soon as you
    modify an HTML or Javascript file, the frontend is restarted). Both are connected. The backend
    runs transparently on port 8080, while the frontend will be automatically displayed in your web
    browser on port 3000.

    The trick here is that gulp serve will automatically route api requests to the backend server,
    (ie, all requests to ``localhost:3000/api`` are proxied to ``localhost:8080/api``), so there is
    no cross origin problem (CORS).

    The backend also serves the production files on port 8080, but you need to have built the
    production frontend first (using ``install:prod`` target). Use this to work on backend routing.
    But in your every day developer life, you probably don't want to use it.

``install:prod`` or ``serve:prod``

    This target will compile the frontend in production mode. ``serve:prod`` will start the
    Python backend in prod mode, ie, it will serve the Angular web site itself.

    Use it for a standalone installation, or to test the production mode on your machine.

- ``install:novirtualenv``

    This target is used when installing Squirrel on a cloud platform that is already a dedicated
    virtual environment (typically, your cloud service actually starts a docker for you).

    For heroku, there are two dedicated targets:

    - ``heroku:build``, used during buildpack creation
    - ``heroku:start``, used to start the production server

Use ``--help`` for full command line help:

.. code-block:: bash

    python install/install.py --help


Installation under Mac OS X and Linux
*************************************

.. note::

    On Mac OS X, this project has been developped and validated with Homebrew.

In the squirrel directory, just execute the following command:

.. code-block:: bash

    python install/install.py


Installation under Windows
**************************

``python.exe`` and ``virtualenv.exe`` should be accessible in your path.

Backend
-------

Please ensure you have pywin32 installed:

Choose in the `Pywin32 website`_ the version matching your version of python (2.7, 3.4, ...) and 32
or 64 bits.

.. _Pywin32 website: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

Windows virtualenv uses ``--system-site-packages`` to access to the ``win32api`` module.

Installation:

.. code-block:: bash

    python.exe -u install\\squirrel-install.py install


Launching unit tests (from outside of virtualenv):

.. code-block:: bash

    install\\unittest.bat squirrel


Building documentation:

.. code-block:: bash

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

Installation:

.. code-block:: bash

    python install/install.py install

Switch to environment (activate virtualenv):

.. code-block:: bash

    source tosource

Leave virtualenv with:

.. code-block:: bash

    deactivate

Clean Virtualenv:

.. code-block:: bash

    python install/uninstall.py

Development
***********

Basically, you just need to run ``install/install.py`` and let all the magic happen. Everything
will be automatically regenerated in development mode:

- frontend (Web UI using Angular)
- backend (Python based)
- online documentation (using sphinx)

Use the following command to build and start the development server:

.. code-block:: bash

    python install/install serve:dev

Your web browser will automatically opens to ``localhost:3000``, with the HTML (frontend) served
by ``gulp serve`` and the backend running with ``squirrel-devbackend``, with ``/api`` automatically
routed so you don't have any CORS issue.

It is advised to have the `BrowserSync <http://www.browsersync.io/>`_ plugin installed in your
browser. With it, any modification done in the frontend will be instantaneously applied into your
web browser.

It also works for the backend, with the ``auto_relauncher`` program deliberately inspired by the
``watchmedo`` demo script from the ``watchdog`` Python module. As soon as a python file, located in
``frontend`` directory, is modified, the backend server is restarted. Just hack and test!

Frontend
--------

Gulp file (re)generation:

.. code-block:: bash

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
- ``gulp protractor:dist`` to launch your e2e tests with Protractor on the dist files

I usually prefer using ``install/install.py start:dev`` target.

Editor configuration
--------------------

I use `SublimeText 3`_  as my main development environment. Here are the custom build command I
have used in this project.

Windows:

.. code-block:: javascript

    "build_systems":
    [
        {
            "cmd":
            [
                "python",
                "-u",
                "install\\install.py",
                "serve:dev"
            ],
            "name": "Squirrel - Install and launch (dev)",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "python",
                "-u",
                "install\\install.py",
                "serve:prod"
            ],
            "name": "Squirrel - Install and launch (prod)",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "python",
                "-u",
                "install\\install.py",
                "start:prod"
            ],
            "name": "Squirrel - Start Prod server (prod). No build!",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "python",
                "-u",
                "install\\uninstall.py"
            ],
            "name": "Squirrel - Uninstall",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "install\\unittest.bat",
                "squirrel"
            ],
            "name": "Squirrel - Unit tests",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "install\\unittest.bat",
                "squirrel_integration_tests"
            ],
            "name": "Squirrel - Integration tests",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "make.bat",
                "html"
            ],
            "name": "Squirrel - Build documentation",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel\\doc"
        },
        {
            "cmd":
            [
                "gulp",
                "build"
            ],
            "name": "Squirrel - Build Frontend",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel\\frontend"
        },
        {
            "cmd":
            [
                "gulp",
                "serve"
            ],
            "name": "Squirrel - Serve Frontend (dev)",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel\\frontend"
        },
        {
            "cmd":
            [
                "python",
                "-u",
                "install\\install.py",
                "serve:devbackend"
            ],
            "name": "Squirrel - Serve backend (dev)",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        },
        {
            "cmd":
            [
                "python",
                "-u",
                "install\\install.py",
                "update:all"
            ],
            "name": "Squirrel - Update all",
            "shell": true,
            "working_dir": "X:\\Path\\to\\Squirrel"
        }
    ],


Linux/Mac OS:

.. code-block:: javascript

    "build_systems":
    [
        {
            "name": "Squirrel - Install and launch",
            "cmd": ["python -u install/install.py "], // add -l to launch Squirrel automatically
            "shell": true,
            "working_dir": "/Full/Path/Where/Is/Installed/Squirrel"
        },
        {
            "name": "Squirrel - Unit test",
            "cmd": ["source workdir/bin/activate && trial squirrel"],
            "shell": true,
            "working_dir": "/Full/Path/Where/Is/Installed/Squirrel"
        },
        {
            "name": "Squirrel - Build documentation",
            "cmd": ["make html"],
            "shell": true,
            "working_dir": "/Full/Path/Where/Is/Installed/Squirrel/doc"
        },
        {
            "name": "Squirrel - Build Frontend",
            "cmd": ["gulp build"],
            "shell": true,
            "working_dir": "/Full/Path/Where/Is/Installed/Squirrel/frontend"
        }
    ]


.. _SublimeText 3: http://www.sublimetext.com/3
