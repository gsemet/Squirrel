#!/bin/env python

import os
import subprocess

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))

with open(config_path) as f:
    config = f.readlines()

print "config", config
install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
requirements_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "requirements.txt"))

print "Installing in {}".format(install_path)
print "Requirements: {}".format(requirements_txt)
print "env", os.environ


virtualenv = "C:\\Python27\\Scripts\\virtualenv.exe"
activate = os.path.join(install_path, "Scripts", "activate.bat")

if not os.path.exists(os.path.join(install_path, "Scripts", "pip.exe")):
    subprocess.call([virtualenv, install_path])

print "Activating virtualenv"
subprocess.call([activate])
