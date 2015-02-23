========
Squirrel
========

Asset Portfolio Management System


Installation
============

Installation is done using the scripts located in the ``install`` directory.

Squirrel runs its own virtuelenv, to avoid

Prerequisits
------------

Have python 2.7, pip and virtualenv installed on your system.

$ python
$ pip
$ pip install virtualenv

Windows
-------

Please ensure you have pywin32 installed:

Choose in http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/ the version
matching your version of python (2.7, 3.4, ...) and 32 or 64 bits.

Windows virtualenv uses ``--system-site-packages`` to access to the win32api module.

Installation::

    python.exe -u install\\squirrel-install.py


Launching unit tests (from outside of virtualenv)::

    install\\unittest.bat squirrel


Building documentation::

    cd doc
    make.bat html



Linux
-----

Installation::

    python install/install.py

Switch to environment (activate virtualenv)::

    source tosource

Leave virtualenv::

    deactivate
