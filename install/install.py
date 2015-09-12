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

import imp
import os
import subprocess
import sys

# Do *not* use optparse or argparse here, we are not sure on which version of python we are!

# Injecting available targets from installer stage 2
stage2 = imp.load_source('install.stage2',
                         os.path.join(os.path.dirname(__file__), "install-stage2.py"))
allowed_cmd = stage2.allowed_cmd
aliases = stage2.aliases

# Injecting available targets from installer stage 2
lib = imp.load_source('install-lib.py',
                      os.path.join(os.path.dirname(__file__), "install-lib.py"))


default_cmd = "install:all"


def usage():
    print("Usage: ./install/install.sh [command]")
    print("")
    print("Commands:")
    for cmd, help in sorted(allowed_cmd.items()):
        print("  {:25}{}".format(cmd, help))
    print("")
    print("Aliases:")
    for alias, cmd in sorted(aliases.items()):
        print("  {:25}{}".format(alias, cmd))
    print("")
    print("If no command is selected, execute the following command: '{}'".format(default_cmd))
    print("")
    print("Uninstall with './install/uninstall.py'")
    sys.exit(0)


def main():
    if len(sys.argv) > 1:
        args = sys.argv[:]
        while args:
            # removing executable name
            args.pop(0)
            subcmd = args.pop(0)
            if subcmd in {"-h", "--help", "help"}:
                usage()
            subcmd = aliases.get(subcmd, subcmd)
            if subcmd not in allowed_cmd.keys():
                lib.printError("Invalid command: {}".format(subcmd))
                lib.printError("Allowed: {}".format(allowed_cmd.keys()))
                lib.printError("See usage with --help")
                sys.exit(1)
    else:
        lib.printInfo("No argument in the command line, using default target: {}".format(default_cmd))
        subcmd = default_cmd

    if sys.version_info < (2, 7):
        raise Exception("must use python 2.7.x. Current version is: {}.".format(sys.version_info))

    if sys.version_info >= (3, 0):
        raise Exception("must use python 2.7.x. Current version is: {}.".format(sys.version_info))

    if "novirtualenv" in subcmd:
        do_virtualenv = False

    do_virtualenv = True
    virtualenv = "virtualenv"

    if lib.isWindows:
        virtualenv = "virtualenv.exe"
        # python_exe = "python.exe"
        launch_in_new_window = True

    if os.environ.get('VIRTUAL_ENV'):
        lib.printError("Beware, you already are inside the following virtual env: {}"
                       .format(os.environ.get('VIRTUAL_ENV')))
        lib.printError("Please leave it with 'deactivate' "
                       "and relaunch your command, unless you understand what is going on.")

    install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))
    stage2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "install-stage2.py"))

    # with open(config_path) as f:
    #     config = f.readlines()

    workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
    requirements_txt = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    os.pardir,
                                                    "requirements.txt"))
    if lib.isWindows:
        activate = os.path.join(workdir_path, "Scripts", "activate.bat")
        activate_info = activate
        os_str = "Windows"
    else:
        activate = os.path.join(workdir_path, "bin", "activate")
        activate_info = "source {0}".format(activate)
        os_str = "Posix"

    lib.printSeparator("=")
    lib.printBoot("Squirrel Installer Stage 1")
    lib.printBoot("Executing command: '{}'".format(subcmd))
    lib.printBoot("Platform: {0}".format(sys.platform))
    lib.printBoot("Environment: {0}".format(os_str))
    lib.printBoot("Interpreter: {0} - Version: {1}".format(sys.executable,
                                                           sys.version.split("\n")[0]))
    if do_virtualenv:
        try:
            lib.printInfo("Checking if virtualenv exits...")
            lib.run([virtualenv, "--version"])
            lib.printInfo("OK")
        except:
            lib.printError("Missing dependency: virtualenv. "
                           "Please install this mandatory dependency!")
            raise

        lib.printBoot("Setting up virtualenv to start Installer Stage 2.")
    else:
        m = "Beware !! 'novirtualenv' mode detected, do ** NOT ** setup a virtual env!"
        lib.printBoot("!" * len(m))
        lib.printBoot(m)
        lib.printBoot("*** Hope your production works inside a Docker !! *** ")
        lib.printBoot("!" * len(m))
    lib.printBoot("You can activate this environment with the following command:")
    lib.printBoot("    {0}".format(activate_info))
    lib.printBoot("Installing in {0}".format(workdir_path))
    lib.printBoot("Requirements: {0}".format(requirements_txt))

    if lib.isWindows:

        if not os.path.exists(os.path.join(workdir_path, "Scripts", "pip.exe")):
            lib.printBoot("Installing virtualenv in: {0}".format(workdir_path))
            try:
                lib.run([virtualenv, "--system-site-packages", workdir_path])
            except:
                lib.printError("Error during installation of virtualenv. Do you have virtual env "
                               "in your system? Install it with:")
                lib.printError("  sudo pip install virtualenv")
                lib.printError("Reraising original exception:")
                raise

        # using launcher instead of activate.bat because we want to launch custom commands
        launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

        lib.printBoot("Activating virtualenv in {0}".format(workdir_path))
        lib.run([
            "cmd", "/K",
            launcher_bat, "new_window" if launch_in_new_window else "no_new_window",
            workdir_path, stage2_path, install_path, workdir_path, subcmd])

    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):

        if do_virtualenv:
            if "VIRTUAL_ENV" in os.environ and not os.environ['VIRTUAL_ENV']:
                lib.printBoot("Note: Already in a virtualenv!")

            activate = os.path.join(workdir_path, "bin", "activate")

            if not os.path.exists(os.path.join(workdir_path, "bin", "pip")):
                lib.run(['virtualenv', workdir_path])

            if not os.path.exists(os.path.join(install_path, "activate")):
                lib.printBoot("Creating symblink activate")
                os.symlink(os.path.join(workdir_path, "bin", "activate"), os.path.join(install_path,
                                                                                       "activate"))

            lib.printBoot("Activating virtualenv in {0}".format(workdir_path))
            # lib.run([python_exe, stage2_path, activate, install_path])
            lib.run([
                'bash',
                '-c',
                'source {activate} && python {stage2} {install_path} {workdir_path} {subcmd}'
                .format(activate=activate,
                        stage2=stage2_path,
                        install_path=install_path,
                        workdir_path=workdir_path,
                        subcmd=subcmd)])
        else:
            lib.printBoot("Starting stage 2 directly without installing a virtualenv")
            # lib.run([python_exe, stage2_path, activate, install_path])
            lib.run([
                'python',
                stage2_path,
                install_path,
                workdir_path,
                subcmd,
            ])

    else:
        raise Exception("Unsupported environment: {0}".format(sys.platform))

if __name__ == "__main__":
    main()
