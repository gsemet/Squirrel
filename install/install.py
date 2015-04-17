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

isWindows = False
if sys.platform.startswith('win32'):
    isWindows = True

do_virtualenv = True

allowed_cmd = {
    "serve:dev": ("install and launch developer server (backend served with auto_relauncher and "
                  "frontend served by 'gulp serve')"),
    "serve:devbackend": ("install and launch only the dev backend (with auto relauncher))"),
    "serve:prod": "install and launch production server",
    "serve:novirtualenv": ("install and serve production without going into "
                           "virtualenv (Docker/Heroku)"),
    "install:backend": "install only backend (python)",
    "install:all": "install backend and frontend",
    "install:novirtualenv": "install backend and frontend without virtualenv",
    "update:all": "update all dependencies (modules installed by npm and bower)",
}
aliases = {"serve": "serve:dev",
           "install": "install:all"}
default_cmd = "install:all"

####################################################################################################
# Utility functions
####################################################################################################


class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOOT = '\033[94m'

    ENDC = '\033[0m'

# Do *not* use color when:
#  - on windows
#  - not in a terminal except if we are in Travis CI
if isWindows or (not os.environ.get("TRAVIS") and not sys.stdout.isatty()):
    bcolors.HEADER = ''
    bcolors.OKBLUE = ''
    bcolors.OKGREEN = ''
    bcolors.WARNING = ''
    bcolors.FAIL = ''
    bcolors.BOLD = ''
    bcolors.UNDERLINE = ''
    bcolors.BOOT = ''
    bcolors.ENDC = ''


def printInfo(text):
    print(bcolors.OKBLUE + "[INFO ] " + bcolors.ENDC + text)


def printError(text):
    print(bcolors.FAIL + "[ERROR] " + bcolors.ENDC + text, file=sys.stderr)


def printSeparator(char="-", color=bcolors.OKGREEN):
    print(color + char * 79 + bcolors.ENDC)


def printNote(text):
    print(bcolors.HEADER + "[NOTE ] " + bcolors.ENDC + text)


def printBoot(text):
    print(bcolors.BOOT + "[BOOT ] " + bcolors.ENDC + text)


def run(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def call(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def run_background(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD (background)" + bcolors.ENDC + "] {}".format(" ".join(cmd)))
    subprocess.Popen(cmd, cwd=cwd, shell=shell)

####################################################################################################


def usage():
    print("Usage: ./install/install.sh [command]")
    print("")
    print("Commands:")
    for cmd, help in sorted(allowed_cmd.items()):
        print("  {:20}{}".format(cmd, help))
    print("")
    print("Aliases:")
    for alias, cmd in sorted(aliases.items()):
        print("  {:10}{}".format(alias, cmd))
    print("")
    print("If no command is selected, execute the following command: '{}'".format(default_cmd))
    print("")
    print("Uninstall with './install/uninstall.py'")
    sys.exit(0)


if len(sys.argv) > 1:
    args = sys.argv[:]
    while args:
        executable = args.pop(0)
        subcmd = args.pop(0)
        if subcmd in {"-h", "--help"}:
            usage()
        subcmd = aliases.get(subcmd, subcmd)
        if subcmd not in allowed_cmd.keys():
            print("Invalid command: {}".format(subcmd))
            print("See usage with --help")
            sys.exit(1)
else:
    print("No argument in the command line, using default target: {}".format(default_cmd))
    subcmd = default_cmd

if sys.version_info < (2, 7):
    raise Exception("must use python 2.7.x. Current version is: {}.".format(sys.version_info))

if sys.version_info >= (3, 0):
    raise Exception("must use python 2.7.x. Current version is: {}.".format(sys.version_info))

if "novirtualenv" in subcmd:
    do_virtualenv = False

if os.environ.get('VIRTUAL_ENV'):
    printError("You are inside a virtual env. Please leave it with 'deactivate' and relaunch "
               "your command")
    sys.exit(1)

install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))
stage2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "install-stage2.py"))

with open(config_path) as f:
    config = f.readlines()

workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
requirements_txt = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                os.pardir,
                                                "requirements.txt"))
if isWindows:
    activate = os.path.join(workdir_path, "Scripts", "activate.bat")
    activate_info = activate
    os_str = "Windows"
else:
    activate = os.path.join(workdir_path, "bin", "activate")
    activate_info = "source {0}".format(activate)
    os_str = "Posix"

printSeparator("=")
printBoot("Squirrel Installer Stage 1")
printBoot("Executing command: '{}'".format(subcmd))
printBoot("Platform: {0}".format(sys.platform))
printBoot("Environment: {0}".format(os_str))
printBoot("Interpreter: {0} - Version: {1}".format(sys.executable, sys.version.split("\n")[0]))
if do_virtualenv:
    printBoot("Setting up virtualenv to start Installer Stage 2.")
else:
    printBoot("!!!!!!!!!!!!!!!!!!!")
    printBoot("Do **NOT** setup a virtual env ('novirtualenv' option). Production on Docker mode.")
    printBoot("!!!!!!!!!!!!!!!!!!!")
printBoot("You can activate this environment with the following command:")
printBoot("    {0}".format(activate_info))
printBoot("Installing in {0}".format(workdir_path))
printBoot("Requirements: {0}".format(requirements_txt))


if isWindows:
    virtualenv = "virtualenv.exe"
    python_exe = "python.exe"
    launch_in_new_window = True

    if not os.path.exists(os.path.join(workdir_path, "Scripts", "pip.exe")):
        print("Installing virtualenv in: {0}".format(workdir_path))
        subprocess.check_call([virtualenv, "--system-site-packages", workdir_path])

    # using launcher instead of activate.bat because we want to launch custom commands
    launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

    printBoot("Activating virtualenv in {0}".format(workdir_path))
    subprocess.check_call([
        "cmd", "/K",
        launcher_bat, "new_window" if launch_in_new_window else "no_new_window",
        workdir_path, stage2_path, install_path, workdir_path, subcmd])

elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):

    if do_virtualenv:
        if "VIRTUAL_ENV" in os.environ and not os.environ['VIRTUAL_ENV']:
            printBoot("Note: Already in a virtualenv!")

        activate = os.path.join(workdir_path, "bin", "activate")

        if not os.path.exists(os.path.join(workdir_path, "bin", "pip")):
            subprocess.check_call(['virtualenv', workdir_path])

        if not os.path.exists(os.path.join(install_path, "activate")):
            printBoot("Creating symblink activate")
            os.symlink(os.path.join(workdir_path, "bin", "activate"), os.path.join(install_path,
                                                                                   "activate"))

        printBoot("Activating virtualenv in {0}".format(workdir_path))
        # subprocess.check_call([python_exe, stage2_path, activate, install_path])
        subprocess.check_call([
            'bash',
            '-c',
            'source {activate} && python {stage2} {install_path} {workdir_path} {subcmd}'
            .format(activate=activate,
                    stage2=stage2_path,
                    install_path=install_path,
                    workdir_path=workdir_path,
                    subcmd=subcmd)])
    else:
        printBoot("Starting stage 2 directly without installing a virtualenv")
        # subprocess.check_call([python_exe, stage2_path, activate, install_path])
        subprocess.check_call([
            'python',
            stage2_path,
            install_path,
            workdir_path,
            subcmd,
        ])

else:
    raise Exception("Unsupported environment: {0}".format(sys.platform))
