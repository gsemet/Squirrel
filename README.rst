========
Squirrel
========

.. image:: https://img.shields.io/travis/Stibbons/python-Squirrel/master.svg
    :target: https://travis-ci.org/Stibbons/python-Squirrel

.. image:: https://img.shields.io/coveralls/Stibbons/python-Squirrel.svg
    :target: https://coveralls.io/r/Stibbons/python-Squirrel


Asset Portfolio Management System.


Installation
============

Installation is done using the scripts located in the ``install`` directory.

Squirrel runs its own virtuelenv, to avoid conflict with installed libraries.

Prerequisits
************

Have python 2.7, pip and virtualenv installed on your system:

.. code-block:: bash

    $ python   # Python 2.7.9
    $ pip  # pip 6.0.8
    $ pip install virtualenv

To build the frontend UI (HTML), you'll need node, bower and gulp.

.. code-block:: bash

    $ npm install -g gulp
    $ npm install -g bower

Installation under Mac OS X and Linux
*************************************

.. note::

    On Mac OS X, this project has been developped and validated with Homebrew.

In the squirrel directory, execute the following command:

.. code-block:: bash

    python install/install.py


Installation under Windows
**************************

``python.exe`` and ``virtualenv.exe`` should be accessible through your path.

Backend
-------

Please ensure you have pywin32 installed:

Choose in the `Pywin32 website`_ the version matching your version of python (2.7, 3.4, ...) and 32
or 64 bits.

.. _Pywin32 website: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

Windows virtualenv uses ``--system-site-packages`` to access to the ``win32api`` module.

Installation:

.. code-block:: bash

    python.exe -u install\\squirrel-install.py


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

    python install/install.py

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
will be automatically regenerated:

- frontend (Web UI using Angular)
- backend (Python based)
- online documentation (using sphinx)

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

Editor configuration
--------------------

I use `SublimeText 3`_  as my main development environment. Here are the custom build command I
have used in this project.

Windows:

.. code-block:: javascript

    "build_systems":
    [
        {
            "name": "Squirrel - Install and launch",
            "cmd": ["python", "-u", "install\\install.py"], // add -l to launch Squirrel automatically
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
