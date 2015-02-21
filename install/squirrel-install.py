#!/bin/env python

import sys
import os
import subprocess

install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))
stage2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "install-stage2.py"))

with open(config_path) as f:
    config = f.readlines()

workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
requirements_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "requirements.txt"))

print "Installing in {}".format(workdir_path)
print "Requirements: {}".format(requirements_txt)

if sys.platform == 'win32':
    virtualenv = "C:\\Python27\\Scripts\\virtualenv.exe"
    python_exe = "C:\\Python27\\python.exe"
    activate = os.path.join(workdir_path, "Scripts", "activate.bat")

    if not os.path.exists(os.path.join(workdir_path, "Scripts", "pip.exe")):
        subprocess.check_call([virtualenv, workdir_path])

    activate_this = os.path.join(workdir_path, "Scripts", "activate.bat")
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    print "Activating virtualenv in {}".format(workdir_path)
    # subprocess.check_call([python_exe, stage2_path, activate_this, install_path])
    subprocess.check_call(["cmd", "/K", launcher_bat, activate_this, stage2_path, install_path, workdir_path])
