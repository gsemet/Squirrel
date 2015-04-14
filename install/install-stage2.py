# This is the second part of the installation procedure or Squirrel.
# It should be executed from the virtualenv

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import os
import subprocess
import sys

from time import sleep

install_path = sys.argv[1]
install_path = os.path.abspath(install_path)

workdir_path = sys.argv[2]
workdir_path = os.path.abspath(workdir_path)

subcmd = sys.argv[3]

allowed_cmd = {
    "serve:dev",
    "serve:prod",
    "serve:novirtualenv",
    "install:backend",
    "install:all",
    "install:novirtualenv",
}

# if not os.environ['VIRTUAL_ENV']:
#     raise Exception("VIRTUAL_ENV environment variable is empty. We are not in a virtualenv.")


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
    BOOT = '\033[97m'

    ENDC = '\033[0m'

# Do *not* use color when not in a terminal
if not sys.stdout.isatty():
    bcolors.HEADER = ''
    bcolors.OKBLUE = ''
    bcolors.OKGREEN = ''
    bcolors.WARNING = ''
    bcolors.FAIL = ''
    bcolors.BOLD = ''
    bcolors.UNDERLINE = ''

    bcolors.ENDC = ''


def printInfo(text):
    print(bcolors.OKBLUE + "[INFO ] " + bcolors.ENDC + text)


def printError(text):
    print(bcolors.FAIL + "[ERROR] " + bcolors.ENDC + text, file=sys.stderr)


def printSeparator(char="-"):
    print(char * 79)


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

printSeparator("=")
printInfo("Squirrel Installer Stage 2")
if subcmd not in allowed_cmd:
    printError("Invalid install target: {}. Available: {}".format(subcmd, allowed_cmd))
    sys.exit(1)
printInfo("We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
printInfo("Interpreter: {0} - Version: {1}".format(sys.executable, sys.version.split("\n")[0]))
printInfo("installation dir: {}".format(install_path))
printInfo("workdir: {}".format(workdir_path))
printInfo("Install target: {}".format(subcmd))
printInfo("Environment variables:")
for k, v in sorted(os.environ.items()):
    printInfo("  {0}:{1}".format(k, v))

printSeparator("=")
printInfo("")
printInfo("Installation process really starts here...")
printInfo("")


if sys.platform.startswith("linux"):
    pip_version_str = str(subprocess.check_output(["pip", "--versio"]))
    pip_version_str = pip_version_str.split(" ")[1]
    pip_version_str = pip_version_str.split("-")[0]
    pip_version_str = pip_version_str.split("_")[0]
    pip_version_str = pip_version_str.rpartition(".")[0]
    pip_major, _, pip_minor = pip_version_str.partition(".")
    pip_version = int(pip_major) * 100 + int(pip_minor)
    if pip_version <= 105:
        printSeparator()
        printInfo("Patching this pip (version) {}.{}), to fix proxy issue (fixed in pip 1.6)"
                  .format(pip_major, pip_minor))
        printInfo("See: https://github.com/pypa/pip/issues/1805")
        # Patching the installed pip to fix the following bug with proxy
        # See http://www.irvingc.com/posts/10
        patch_path = os.path.join(install_path, "install", "patch-pip.patch")
        c = call(["bash", "-c", "patch -p0 -N --dry-run --silent < {} 2>/dev/null"
                  .format(patch_path)])
        if not c:
            printInfo("Applying patch")
            run(["bash", "-c", "patch -p0 < {}".format(patch_path)])
        else:
            printInfo("Already applied. Skipping patch")

printSeparator()
printInfo("Updating pip (try to always use latest version of pip)")
printInfo("cd backend")
run(["pip", "install", "--upgrade", "pip"])

printSeparator()
printInfo("Installing backend requirements")
printInfo("cd backend")
run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                          "requirements.txt")])

if sys.version_info < (3, 4):
    printInfo("Python version {}.{} < 3.4, installing extra requirements"
              .format(sys.version_info[0], sys.version_info[2]))
    printInfo("cd backend")
    run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                              "requirements-py_lt34.txt")])

if sys.platform.startswith('win32'):
    printSeparator()
    printInfo("Installing Windows dependencies")
    run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                              "requirements-win32.txt")])
    printInfo("Ensure you have win32api installed")


printSeparator()
printInfo("Installing backend")
printInfo("cd backend")
run(["pip", "install", "-e", os.path.join(install_path, "backend")])

if sys.platform.startswith('win32'):
    shell = True
else:
    shell = False

if subcmd != "install:backend":
    printSeparator()
    printInfo("Compiling frontend website")
    if "http_proxy" in os.environ:
        printInfo("Behind a proxy: npm --proxy")
        printNote("You may want to add the following lines in your ~/.gitconfig:")
        printNote("   [url \"https://github.com\"]")
        printNote("      insteadOf=git://github.com")
        printInfo("cd frontend")
        run(["npm", "config", "set", "strict-ssl", "false"], cwd=os.path.join(install_path,
                                                                              "frontend"),
            shell=shell)
        printInfo("cd frontend")
        run(["npm", "--proxy", os.environ["http_proxy"], "install"], cwd=os.path.join(install_path,
                                                                                      "frontend"),
            shell=shell)
    else:
        printInfo("cd frontend")
        run(["npm", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    printInfo("cd frontend")
    run(["bower", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    if subcmd != "serve:dev":
        printInfo("cd frontend")
        run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    printSeparator()
    printInfo("Building online documentation")
    if sys.platform.startswith('win32'):
        run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"), shell=True)
    else:
        run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)

if subcmd.startswith("install"):
    print("")
    printSeparator()
    print("Do not start the server. Install is succesful.")
    printSeparator()
    sys.exit(0)

printSeparator()
if subcmd == "serve:prod":
    # Launching Squirrel-server
    if sys.platform.startswith('win32'):
        backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-server.exe")
    else:
        backend_launcher = "squirrel-server"
    printInfo("Launching Squirrel-server {}".format(backend_launcher))
    sys.stdout.flush()
    sys.stderr.flush()

    run([backend_launcher])

elif subcmd == "serve:dev":
    # Launching Squirrel-devbackend, which doesn't serve the front end, and let the front
    # be served by 'gulp serve'
    if sys.platform.startswith('win32'):
        devbackend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-devbackend.exe")
    else:
        devbackend_launcher = "squirrel-devbackend"
    printInfo("Launching squirrel-devbackend {}".format(devbackend_launcher))
    sys.stdout.flush()
    sys.stderr.flush()

    run_background([devbackend_launcher])
    printInfo("Sleep 5 seconds")
    sys.stdout.flush()
    sys.stderr.flush()
    sleep(5)

    printInfo("Serving dev frontend")
    run(["gulp", "serve"], cwd=os.path.join(install_path, "frontend"), shell=shell)


printInfo("Done")
printSeparator()
