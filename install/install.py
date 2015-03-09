#!/usr/bin/env python

# Beware:
#  - this script is executed using the system's python, so with not easy control on which
#    packages are available. Same, we cannot directly install new ones using pip.
#  - the role of the first stage of this installer is just to install a fresh new virtualenv
#    with a *controled* version of python, pip and virtualenv, and launch the second part of
#    the installer, 'install-stage2.py', which will run in the virtualenv.

# Note:
#  - I try to keep this installer python-2.6 friendly, but I really encourage you to install
#    Python 2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess
import sys

if sys.version_info < (2, 7):
    raise "must use python 2.7.x. Current version is: {}.".format(sys.version_info)

if sys.version_info >= (3, 0):
    raise "must use python 2.7.x. Current version is: {}.".format(sys.version_info)

install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))
stage2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "install-stage2.py"))

with open(config_path) as f:
    config = f.readlines()

workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
requirements_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "requirements.txt"))

print("Installing in {0}".format(workdir_path))
print("Requirements: {0}".format(requirements_txt))

if sys.platform.startswith('win32'):
    virtualenv = "virtualenv.exe"
    python_exe = "python.exe"
    launch_in_new_window = True
    activate = os.path.join(workdir_path, "Scripts", "activate.bat")

    if not os.path.exists(os.path.join(workdir_path, "Scripts", "pip.exe")):
        print("Installing virtualenv in: {0}".format(workdir_path))
        subprocess.check_call([virtualenv, "--system-site-packages", workdir_path])

    activate = os.path.join(workdir_path, "Scripts", "activate.bat")
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    print("Activating virtualenv in {0}".format(workdir_path))
    # subprocess.check_call([python_exe, stage2_path, activate, install_path])
    subprocess.check_call([
        "cmd", "/K",
        launcher_bat, "new_window" if launch_in_new_window else "no_new_window",
        workdir_path, stage2_path, install_path, workdir_path])

elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    activate = os.path.join(workdir_path, "bin", "activate")
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    if not os.path.exists(os.path.join(workdir_path, "bin", "pip")):
        subprocess.check_call(['virtualenv', workdir_path])

    if not os.path.exists(os.path.join(install_path, "tosource")):
        print("Creating symblink tosource")
        os.symlink(os.path.join(workdir_path, "bin", "activate"), os.path.join(install_path,
                                                                               "tosource"))

    print("Activating virtualenv in {0}".format(workdir_path))
    # subprocess.check_call([python_exe, stage2_path, activate, install_path])
    subprocess.check_call(['bash',
                           '-c',
                           'source {activate} && python {stage2} {install_path} {workdir_path}'
                           .format(activate=activate,
                                   stage2=stage2_path,
                                   install_path=install_path,
                                   workdir_path=workdir_path)])


else:
    raise Exception("Unsupported environment: {0}".format(sys.platform))
