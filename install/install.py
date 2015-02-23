#!/usr/bin/env python

# Beware:
#  - this script is executed using the system's python, so with not easy control on which
#    packages are available. Same, we cannot directly install new ones using pip.
#  - the role of the first stage of this installer is just to install a fresh new virtualenv
#    with a *controled* version of python, pip and virtualenv, and launch the second part of
#    the installer, 'install-stage2.py', which will run in the virtualenv.

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
        subprocess.check_call([virtualenv, "--system-site-packages", workdir_path])

    activate = os.path.join(workdir_path, "Scripts", "activate.bat")
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    print "Activating virtualenv in {}".format(workdir_path)
    # subprocess.check_call([python_exe, stage2_path, activate, install_path])
    subprocess.check_call(["cmd", "/K", launcher_bat, activate, stage2_path, install_path, workdir_path])

elif sys.platform == "linux2":
    activate = os.path.join(workdir_path, "bin", "activate")
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    if not os.path.exists(os.path.join(workdir_path, "bin", "pip")):
        subprocess.check_call(['virtualenv', workdir_path])

    print "Activating virtualenv in {}".format(workdir_path)
    # subprocess.check_call([python_exe, stage2_path, activate, install_path])
    subprocess.check_call(['bash',
                           '-c',
                           'source {activate} && python {stage2} {install_path} {workdir_path}'
                           .format(activate=activate,
                                   stage2=stage2_path,
                                   install_path=install_path,
                                   workdir_path=workdir_path)])

    os.symlink(os.path.join(workdir_path, "bin", "activate", "tosource"))

else:
    raise Exception("Unsupported environment: {}".format(sys.platform))
