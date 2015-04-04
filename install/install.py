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
# Do *not* use optparse or argparse here, we are not sure on which version of python we are!

do_virtualenv = True

if len(sys.argv) > 1:
    args = sys.argv[:]
    while args:
        executable = args.pop(0)
        cmd = args.pop(0)
        if cmd == "-l":
            do_launch = "server"
        elif cmd == "-d":
            do_launch = "dev-server"
        elif cmd == "-b":
            do_launch = "install_only_backend"
        elif cmd == "-n":
            do_launch = "only_install"
            do_virtualenv = False
        elif cmd == "-np":
            do_launch = "server"
            do_virtualenv = False
        elif cmd == "-h":
            print("Usage: ./install/install.sh [-l|-d|-b|-h]")
            print("")
            print("  -l  launch production server")
            print("  -d  launch developer server (backend served normally but frontend served by 'gulp serve'")
            print("  -b  only install backend")
            print("  -n  install production without going into virtualenv (Docker/Heroku)")
            print("  -h  this help message")
            print("")
            print("Uninstall with './install/uninstall.py'")
            sys.exit(0)
        else:
            raise Exception("Invalid parameter: {!r}".format(cmd))
else:
    do_launch = "only_install"

if sys.version_info < (2, 7):
    raise Exception("must use python 2.7.x. Current version is: {}.".format(sys.version_info))

if sys.version_info >= (3, 0):
    raise Exception("must use python 2.7.x. Current version is: {}.".format(sys.version_info))

install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))
stage2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "install-stage2.py"))

with open(config_path) as f:
    config = f.readlines()

workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
requirements_txt = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                os.pardir,
                                                "requirements.txt"))
if sys.platform.startswith('win32'):
    activate = os.path.join(workdir_path, "Scripts", "activate.bat")
    activate_info = activate
    os_str = "Windows"
else:
    activate = os.path.join(workdir_path, "bin", "activate")
    activate_info = "source {0}".format(activate)
    os_str = "Posix"

print("===============================================================================")
print("[BOOT] Squirrel Installer Stage 1")
print("[BOOT] Environment: {0}".format(os_str))
print("[BOOT] Interpreter: {0} - Version: {1}".format(sys.executable, sys.version.split("\n")[0]))
if do_virtualenv:
    print("[BOOT] Setting up virtualenv to start Installer Stage 2.")
else:
    print("[BOOT] Do **NOT** setup a virtual env (-n option). Production on Docker mode.")
print("[BOOT] You can activate this environment with the following command:")
print("[BOOT]     {0}".format(activate_info))
print("[BOOT] Installing in {0}".format(workdir_path))
print("[BOOT] Requirements: {0}".format(requirements_txt))
print("[BOOT] Post installation option: {0}".format(do_launch))


if sys.platform.startswith('win32'):
    virtualenv = "virtualenv.exe"
    python_exe = "python.exe"
    launch_in_new_window = True

    if not os.path.exists(os.path.join(workdir_path, "Scripts", "pip.exe")):
        print("Installing virtualenv in: {0}".format(workdir_path))
        subprocess.check_call([virtualenv, "--system-site-packages", workdir_path])

    # using launcher instead of activate.bat because we want to launch custom commands
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    print("[BOOT] Activating virtualenv in {0}".format(workdir_path))
    subprocess.check_call([
        "cmd", "/K",
        launcher_bat, "new_window" if launch_in_new_window else "no_new_window",
        workdir_path, stage2_path, install_path, workdir_path,
        do_launch])

elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):

    if do_virtualenv:
        if "VIRTUAL_ENV" in os.environ and not os.environ['VIRTUAL_ENV']:
            print("[BOOT] Note: Already in a virtualenv!")

        activate = os.path.join(workdir_path, "bin", "activate")

        if not os.path.exists(os.path.join(workdir_path, "bin", "pip")):
            subprocess.check_call(['virtualenv', workdir_path])

        if not os.path.exists(os.path.join(install_path, "tosource")):
            print("[BOOT] Creating symblink tosource")
            os.symlink(os.path.join(workdir_path, "bin", "activate"), os.path.join(install_path,
                                                                                   "tosource"))

        print("[BOOT] Activating virtualenv in {0}".format(workdir_path))
        # subprocess.check_call([python_exe, stage2_path, activate, install_path])
        subprocess.check_call([
            'bash',
            '-c',
            'source {activate} && python {stage2} {install_path} {workdir_path} {launch}'
            .format(activate=activate,
                    stage2=stage2_path,
                    install_path=install_path,
                    workdir_path=workdir_path,
                    launch=do_launch)])
    else:
        print("[BOOT] Starting stage 2 directly without installing a virtualenv")
        # subprocess.check_call([python_exe, stage2_path, activate, install_path])
        subprocess.check_call([
            'bash',
            '-c',
            'python {stage2} {install_path} {workdir_path} {launch}'
            .format(stage2=stage2_path,
                    install_path=install_path,
                    workdir_path=workdir_path,
                    launch=do_launch)])

else:
    raise Exception("Unsupported environment: {0}".format(sys.platform))
