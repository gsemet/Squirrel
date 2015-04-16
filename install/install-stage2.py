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

cmd_capabilities = {
    "serve:dev": {
        "backend_install",
        "frontend_install",
        "serve",
        "serve_dev",
        "serve_dev_backend",
        "serve_dev_frontend",
    },
    "serve:devbackend": {
        "backend_install",
        "serve",
        "serve_dev",
        "serve_dev_backend",
    },
    "serve:prod": {
        "backend_install",
        "frontend_install",
        "frontend_gulp_build",
        "serve",
        "serve_prod",
    },
    "serve:novirtualenv": {
        "backend_install",
        "frontend_install",
        "frontend_gulp_build",
        "serve",
        "serve_prod",
    },
    "install:backend": {
        "backend_install",
        "frontend_install"
    },
    "install:all": {
        "backend_install",
        "frontend_install",
        "frontend_gulp_build",
    },
    "install:novirtualenv": {
        "backend_install",
        "frontend_install",
        "frontend_gulp_build",
    },
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
    BOOT = '\033[94m'

    ENDC = '\033[0m'

# Do *not* use color when:
#  - on windows
#  - not in a terminal except if we are in Travis CI
if sys.platform.startswith('win32') or (not os.environ.get("TRAVIS") and not sys.stdout.isatty()):
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
    sys.stdout.flush()
    sys.stderr.flush()


def printError(text):
    print(bcolors.FAIL + "[ERROR] " + bcolors.ENDC + text, file=sys.stderr)
    sys.stdout.flush()
    sys.stderr.flush()


def printSeparator(char="-", color=bcolors.OKGREEN):
    print(color + char * 79 + bcolors.ENDC)
    sys.stdout.flush()
    sys.stderr.flush()


def printNote(text):
    print(bcolors.HEADER + "[NOTE ] " + bcolors.ENDC + text)
    sys.stdout.flush()
    sys.stderr.flush()


def printBoot(text):
    print(bcolors.BOOT + "[BOOT ] " + bcolors.ENDC + text)
    sys.stdout.flush()
    sys.stderr.flush()


def run(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    sys.stdout.flush()
    sys.stderr.flush()
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def call(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    sys.stdout.flush()
    sys.stderr.flush()
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def run_background(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD (background)" + bcolors.ENDC + "] {}".format(" ".join(cmd)))
    sys.stdout.flush()
    sys.stderr.flush()
    subprocess.Popen(cmd, cwd=cwd, shell=shell)

####################################################################################################

printSeparator("=")
printInfo("Squirrel Installer Stage 2")
if subcmd not in cmd_capabilities.keys():
    printError("Invalid install target: {}. Available: {}".format(subcmd, cmd_capabilities.keys()))
    sys.exit(1)
current_capabilities = cmd_capabilities[subcmd]
printInfo("We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
printInfo("Interpreter: {0} - Version: {1}".format(sys.executable, sys.version.split("\n")[0]))
printInfo("installation dir: {}".format(install_path))
printInfo("workdir: {}".format(workdir_path))
printInfo("Install target: {}".format(subcmd))
printInfo("Install Capabilities: {}".format(", ".join(sorted(list(current_capabilities)))))
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

if "frontend_install" in current_capabilities:
    printSeparator()
    printInfo("Compiling frontend website")
    if "http_proxy" in os.environ:
        printNote("Behind a proxy: npm --proxy")
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

    if "frontend_gulp_build" in current_capabilities:
        printInfo("cd frontend")
        run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    printSeparator()
    printInfo("Building online documentation")
    if sys.platform.startswith('win32'):
        run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"), shell=True)
    else:
        run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)

if "serve" not in current_capabilities:
    print("")
    printSeparator()
    print("Do not start the server. Install is succesful.")
    printSeparator()
    sys.exit(0)

printSeparator()
if "serve_prod" in current_capabilities:
    # Launching Squirrel-server
    if sys.platform.startswith('win32'):
        backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-server.exe")
    else:
        backend_launcher = "squirrel-server"
    printInfo("Launching Squirrel-server {}".format(backend_launcher))

    run([backend_launcher])

elif "serve_dev" in current_capabilities:
    # Launching Squirrel-devbackend, which doesn't serve the front end, and let the front
    # be served by 'gulp serve'
    if sys.platform.startswith('win32'):
        devbackend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-devbackend.exe")
    else:
        devbackend_launcher = "squirrel-devbackend"
    if "serve_dev_backend" in current_capabilities:
        printInfo("Launching squirrel-devbackend with auto relauncher {}".format(devbackend_launcher))
        sys.stdout.flush()
        sys.stderr.flush()

        sleep_sec = 1
        if sys.platform.startswith('win32'):
            sleep_sec = 5

        if "serve_dev_frontend" in current_capabilities:
            run_background(["auto_relauncher", "--directory", "backend", "--recursive",
                            "--sleep-between-restart", str(sleep_sec), "--patterns", "*.py",
                            devbackend_launcher],
                           cwd=install_path)
        else:
            run(["auto_relauncher", "--directory", "backend", "--recursive",
                 "--sleep-between-restart", str(sleep_sec), "--patterns", "*.py",
                 devbackend_launcher],
                cwd=install_path)
    if (("serve_dev_frontend" in current_capabilities)
            and ("serve_dev_backend" in current_capabilities)):
        printInfo("Sleep 5 seconds")
        sys.stdout.flush()
        sys.stderr.flush()
        sleep(5)

    if "serve_dev_frontend":
        printInfo("Serving dev frontend")
        run(["gulp", "serve"], cwd=os.path.join(install_path, "frontend"), shell=shell)


printInfo("Done")
printSeparator()
