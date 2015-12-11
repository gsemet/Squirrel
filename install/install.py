#!/usr/bin/env python3

# Beware:
#  - this script is executed using the system's python, so with not easy control on which
#    packages are available. Same, we cannot directly install new ones using pip.
#  - the role of the first stage of this installer is just to install a fresh new virtualenv
#    with a *controled* version of python, pip and virtualenv, and launch the second part of
#    the installer, 'install-stage2.py', which will run in the virtualenv.

# Note:
#  - This installer in meant to be compatible with 2.7 and 3.4
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import imp
import os
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
    python_exe = "python3"
    pip_exe = "pip"
    virtualenv_exe = "virtualenv"
    if lib.isMacOsX:
        virtualenv_exe = "virtualenv-3.4"

    if len(sys.argv) > 1:
        args = sys.argv[:]
        while args:
            # removing executable name
            exe_name = args.pop(0)
            subcmd = args.pop(0)
            if subcmd in {"-h", "--help", "help"}:
                usage()
            subcmd = aliases.get(subcmd, subcmd)
            if subcmd not in allowed_cmd.keys():
                lib.printError("Invalid command: {}".format(subcmd))
                lib.printError("Allowed:\n{}".format("\n".join(["  {}".format(c)
                                                                for c
                                                                in sorted(allowed_cmd.keys())])))
                lib.printError("See usage with '{} --help'".format(exe_name))
                sys.exit(1)
    else:
        lib.printInfo("No argument in the command line, using default target: {}"
                      .format(default_cmd))
        subcmd = default_cmd

    if (sys.version_info < (2, 7) or (sys.version_info >= (3, 0) and
                                      sys.version_info <= (3, 3))):
        raise Exception("You must use Python >= 2.7.x or Python >= 3.4 Current version is: {}."
                        .format(sys.version_info))

    do_virtualenv = True

    if "novirtualenv" in subcmd:
        do_virtualenv = False

    if lib.isWindows:
        virtualenv_exe = "virtualenv.exe"
        # python_exe = "python.exe"
        launch_in_new_window = True

    if do_virtualenv and os.environ.get('VIRTUAL_ENV'):
        lib.printError("Beware, you already are inside the following virtual env: {}"
                       .format(os.environ.get('VIRTUAL_ENV')))
        lib.printError("Please leave it with 'deactivate' "
                       "and relaunch your command, unless you understand what is going on.")

    install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
    #                                            "configs", "default.conf"))
    stage2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "install-stage2.py"))

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
            lib.run([virtualenv_exe, "--version"])
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
        pip_exe = "pip.exe"
        python_exe = "python.exe"
        if not os.path.exists(os.path.join(workdir_path, "Scripts", pip_exe)):
            lib.printBoot("Installing virtualenv in: {0}".format(workdir_path))
            try:
                lib.run([virtualenv_exe, "--system-site-packages", workdir_path])
            except:
                lib.printError("Error during installation of virtualenv. Do you have virtual env "
                               "in your system? Install it with:")
                lib.printError("  sudo {pip} install virtualenv".format(pip=pip_exe))
                lib.printError("Reraising original exception:")
                raise

        # using launcher instead of activate.bat because we want to launch custom commands
        launcher_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "launcher.bat"))

        lib.printBoot("Activating virtualenv in {0}".format(workdir_path))
        lib.run([
            "cmd", "/K",
            launcher_bat, "new_window" if launch_in_new_window else "no_new_window",
            workdir_path, stage2_path, install_path, workdir_path, subcmd])

    elif lib.isLinux or lib.isMacOsX:
        if do_virtualenv:
            if "VIRTUAL_ENV" in os.environ and not os.environ['VIRTUAL_ENV']:
                lib.printBoot("Note: Already in a virtualenv!")

            activate = os.path.join(workdir_path, "bin", "activate")
            lib.printInfo("Do {} exists?".format(os.path.join(workdir_path, "bin", pip_exe)))
            if not os.path.exists(os.path.join(workdir_path, "bin", pip_exe)):
                virtualenv_exe = "virtualenv-3.4"
                if lib.executableExists(virtualenv_exe):
                    lib.printInfo("Executing {}".format(virtualenv_exe))
                    lib.run([virtualenv_exe, workdir_path])
                else:
                    virtualenv_exe = "virtualenv"
                    lib.printInfo("Fallback to use virtual --python")
                    lib.run([virtualenv_exe,
                             "--python={python_path}".format(
                                 python_path=str(lib.run_output("which {}".format(python_exe),
                                                                shell=True)).strip()),
                             workdir_path])

            if not os.path.exists(os.path.join(install_path, "activate")):
                lib.printBoot("Creating symblink activate")
                os.symlink(os.path.join(workdir_path, "bin", "activate"), os.path.join(install_path,
                                                                                       "activate"))

            lib.printBoot("Activating virtualenv in {0}".format(workdir_path))
            # lib.run([python_exe, stage2_path, activate, install_path])
            lib.run([
                'bash',
                '-c',
                'source {activate} && {python} {stage2} {install_path} {workdir_path} {subcmd}'
                .format(python=python_exe,
                        activate=activate,
                        stage2=stage2_path,
                        install_path=install_path,
                        workdir_path=workdir_path,
                        subcmd=subcmd)])
        else:
            lib.printBoot("Starting stage 2 directly without installing a virtualenv")
            # lib.run([python_exe, stage2_path, activate, install_path])
            lib.run([
                python_exe,
                stage2_path,
                install_path,
                workdir_path,
                subcmd,
            ])

    else:
        raise Exception("Unsupported environment: {0}".format(sys.platform))

if __name__ == "__main__":
    main()
