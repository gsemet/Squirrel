# This is the second part of the installation procedure or Squirrel.
# It should be executed from the virtualenv
# But beware, you might not have all the wonderful packages you will install with pip yet.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import os
import subprocess
import sys

from time import sleep

isWindows = False
if sys.platform.startswith('win32'):
    isWindows = True

__all__ = ['allowed_cmd', 'aliases']

allowed_cmd = {
    "help":                     "print help message",
    "serve:dev":               ("install and launch developer server (backend served with "
                                "auto_relauncher and frontend and homepage both served by "
                                "'gulp serve')"),
    "serve:dev:backend":       ("install and launch only the dev backend (with auto relauncher))"),
    "serve:dev:frontend":      ("install and launch only the dev frontend (with gulp serve))"),
    "serve:dev:homepage":      ("install and launch only the dev homepage (with gulp serve))"),
    "serve:staging":            "install and server only the staging frontend",
    "serve:prod":               "install and launch production server",
    "serve:novirtualenv":      ("install and serve production without going into "
                                "virtualenv (Docker/Heroku)"),
    "start:prod":              ("start all prod servers (no install)"),
    "start:staging":           ("start all staging servers (no install)"),
    "start:dev":               ("start frontend, homepage and backend dev servers (no install)"),
    "start:dev:frontend":      ("start frontend in dev mode (no install)"),
    "start:dev:homepage":      ("start homepage in dev mode (no install)"),
    "start:dev:backend":       ("start backend in dev mode (no install)"),
    "start:novirtualenv":      ("start all prod servers without virtualenv (heroku model)"),
    "start:novirtualenv:web":  ("start web process only, without virtualenv (heroku model)"),
    "install:backend":          "build/install only backend (python)",
    "install:frontend":         "build/install only frontend (angular)",
    "install:homepage":         "build/install only homepage (angular)",
    "install:all":              "build/install backend and frontend",
    "install:novirtualenv":     "build/install only frontend without virtualenv (heroku model)",
    "update:all":              ("update all dependencies (modules installed by npm and bower) "
                                "and translations"),
    "update:lang:all":          "update all translations files - requires 'poedit'",
    "update:lang:en":           "update translation (en) - requires 'poedit'",
    "update:lang:fr":           "update translation (fr) - requires 'poedit'",
    "test:all":                ("execute all tests (unit tests, integration tests, e2e tests)"),
    "test:unit":               ("execute unit tests"),
    "test:integration":        ("execute unit tests"),
    "test:e2e":                ("execute end to end tests"),
}
aliases = {
    "(empty)": "install:all",
    "serve": "serve:dev",
    "serve:homepage": "serve:dev:homepage",
    "serve:frontend": "serve:dev:frontend",
    "serve:backend": "serve:dev:backend",
    "dev": "serve:dev",
    "start": "start:dev",
    "install": "install:all",
    "build": "install:all",
    "build:all": "install:all",
    "build:homepage": "install:homepage",
    "build:frontend": "install:frontend",
    "install:prod": "install:all",
    "update": "update:all",
    "update:lang": "update:lang:all",
    "test": "test:all",
    "heroku:build": "install:novirtualenv",
    "heroku:start": "start:novirtualenv",
    "heroku:start:web": "start:novirtualenv:web",
}

cmd_capabilities = {
    "help": {
        "help",
    },
    "serve:dev": {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "homepage_install",
        "serve",
        "serve_dev",
        "serve_dev_backend",
        "serve_dev_frontend",
        "serve_dev_homepage",
    },
    "serve:dev:backend": {
        "pip_upgrade",
        "backend_install",
        "serve",
        "serve_dev",
        "serve_dev_backend",
    },
    "serve:dev:frontend": {
        "pip_upgrade",
        "frontend_install",
        "serve",
        "serve_dev",
        "serve_dev_frontend",
    },
    "serve:dev:homepage": {
        "pip_upgrade",
        "frontend_install",
        "serve",
        "serve_dev",
        "serve_dev_homepage",
    },
    "serve:prod": {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "homepage_install",
        "frontend_gulp_build",
        "homepage_gulp_build",
        "serve",
        "serve_prod",
    },
    "serve:staging": {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "frontend_gulp_build",
        "homepage_install",
        "homepage_gulp_build",
        "serve",
        "serve_staging",
    },
    "serve:novirtualenv": {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "frontend_gulp_build",
        "homepage_install",
        "homepage_gulp_build",
        "serve",
        "serve_prod",
        "novirtualenv",
        "heroku",
    },
    "start:prod": {
        "serve",
        "serve_prod",
    },
    "start:staging": {
        "serve",
        "serve_staging",
    },
    "start:dev": {
        "serve",
        "serve_dev",
        "serve_dev_backend",
        "serve_dev_frontend",
        "serve_dev_homepage",
    },
    "start:dev:frontend": {
        "serve",
        "serve_dev",
        "serve_dev_frontend",
    },
    "start:dev:homepage": {
        "serve",
        "serve_dev",
        "serve_dev_homepage",
    },
    "start:dev:backend": {
        "serve",
        "serve_dev",
        "serve_dev_backend",
    },
    "start:novirtualenv": {
        "serve",
        "serve_prod",
        # TODO: add worker server here when it will be splitted
        "novirtualenv",
        "heroku",
    },
    "start:novirtualenv:web": {
        "serve",
        "serve_prod",
        "novirtualenv",
        "heroku",
    },
    "install:all": {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "homepage_install",
        "frontend_gulp_build",
        "homepage_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:backend": {
        "pip_upgrade",
        "backend_install",
        "warn_no_serve_and_quit",
    },
    "install:frontend": {
        "frontend_install",
        "frontend_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:homepage": {
        "homepage_install",
        "homepage_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:novirtualenv": {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "homepage_install",
        "novirtualenv",
        "warn_no_serve_and_quit",
    },
    'update:all': {
        "pip_upgrade",
        "backend_install",
        "frontend_install",
        "frontend_update",
        "frontend_update_npm",
        "frontend_update_bower",
        "frontend_gulp_build",
        "frontend_update_translations_fr",
        "frontend_update_translations_en",
        "homepage_install",
        "homepage_update",
        "homepage_update_npm",
        "homepage_update_bower",
        "homepage_gulp_build",
        "homepage_update_translations_fr"
        "homepage_update_translations_en"
    },
    'update:lang:all': {
        "pip_upgrade",
        "backend_install",
        "backend_update_translation",
        "frontend_install",
        "frontend_gulp_build",
        "frontend_update_translations_fr",
        "frontend_update_translations_en",
        "homepage_install",
        "homepage_gulp_build",
        "homepage_update_translations_fr",
        "homepage_update_translations_en",
        # add all update cap here
    },
    'update:lang:fr': {
        "pip_upgrade",
        "backend_install",
        "backend_update_translation",
        "frontend_install",
        "frontend_gulp_build",
        "frontend_update_translations_fr",
        "homepage_install",
        "homepage_gulp_build",
        "homepage_update_translations_fr",
    },
    'update:lang:en': {
        "pip_upgrade",
        "backend_install",
        "backend_update_translation",
        "frontend_install",
        "frontend_gulp_build",
        "frontend_update_translations_en",
        "homepage_install",
        "homepage_gulp_build",
        "homepage_update_translations_en",
    },
    "test:all": {
        "test",
        "backend_test_unit",
        "backend_test_integration",
    },
    "test:unit": {
        "test",
        "backend_test_unit",
    },
    "test:integration": {
        "test",
        "backend_test_integration",
    },
    "test:e2e": {
        "test",
        "frontend_test_e2e",
        "homepage_test_e2e",
    },
}

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


def flush():
    sys.stdout.flush()
    sys.stderr.flush()


def printInfo(text):
    print(bcolors.OKBLUE + "[INFO ] " + bcolors.ENDC + text)
    flush()


def printError(text):
    print(bcolors.FAIL + "[ERROR] " + bcolors.ENDC + text, file=sys.stderr)
    flush()


def printSeparator(char="-", color=bcolors.OKGREEN):
    print(color + char * 79 + bcolors.ENDC)
    flush()


def printNote(text):
    print(bcolors.HEADER + "[NOTE ] " + bcolors.ENDC + text)
    flush()


def printBoot(text):
    print(bcolors.BOOT + "[BOOT ] " + bcolors.ENDC + text)
    flush()


def run(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def call(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def run_background(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD (background)" + bcolors.ENDC + "] {}".format(" ".join(cmd)))
    flush()
    subprocess.Popen(cmd, cwd=cwd, shell=shell)

####################################################################################################


def main():

    install_path = sys.argv[1]
    install_path = os.path.abspath(install_path)

    workdir_path = sys.argv[2]
    workdir_path = os.path.abspath(workdir_path)

    subcmd = sys.argv[3]

    printSeparator("=")
    printInfo("Squirrel Installer Stage 2")
    if subcmd not in cmd_capabilities.keys():
        printError("Invalid install target: {}. Available: {}"
                   .format(subcmd, cmd_capabilities.keys()))
        sys.exit(1)
    current_capabilities = cmd_capabilities[subcmd]
    if "help" in current_capabilities:
        printInfo("Help")
        return 0
    if "VIRTUAL_ENV" not in os.environ:
        printInfo("We are **NOT** in a virtualenv")
    else:
        printInfo("We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
    printInfo("Interpreter: {0} - Version: {1}".format(sys.executable, sys.version.split("\n")[0]))
    printInfo("installation dir: {}".format(install_path))
    printInfo("workdir: {}".format(workdir_path))
    printInfo("Executing command: '{}'".format(subcmd))
    printInfo("Install Capabilities: {}".format(", ".join(sorted(list(current_capabilities)))))
    printInfo("Environment variables:")
    for k, v in sorted(os.environ.items()):
        printInfo("  {0}:{1}".format(k, v))

    printSeparator("=")
    printInfo("")
    printInfo("Installation process really starts here...")
    printInfo("")

    if isWindows:
        shell = True
        activate_path = os.path.join(workdir_path, "Scripts", "activate.exe")
    else:
        shell = False
        activate_path = os.path.join(workdir_path, "bin", "activate")

    if "pip_upgrade" in current_capabilities:
        if sys.platform.startswith("linux"):
            pip_version_str = str(subprocess.check_output(["pip", "--version"]))
            pip_version_str = pip_version_str.split(" ")[1]
            pip_version_str = pip_version_str.split("-")[0]
            pip_version_str = pip_version_str.split("_")[0]
            pip_version_str = pip_version_str.rpartition(".")[0]
            pip_major, _, pip_minor = pip_version_str.partition(".")
            pip_minor = pip_minor.partition('.')[0]
            pip_minor = pip_minor.partition('-')[0]
            pip_version = int(pip_major) * 100 + int(pip_minor)
            if pip_version <= 105:
                printSeparator()
                printInfo("Patching this pip (version) {}.{}), "
                          "to fix proxy issue (fixed in pip 1.6)"
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

    if "backend_install" in current_capabilities:
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

        if isWindows:
            printSeparator()
            printInfo("Installing Windows dependencies")
            run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                                      "requirements-win32.txt")])
            printInfo("Ensure you have win32api installed")

        printSeparator()
        printInfo("Installing backend")
        printInfo("cd backend")
        run(["pip", "install", "-e", os.path.join(install_path, "backend")])

    if "frontend_install" in current_capabilities:
        printSeparator()
        printInfo("Compiling frontend website")
        printInfo("PWD")
        run(["bash", "-c", "echo PWD=$PWD"])
        run(["bash", "-c", "echo PATH=$PATH"])
        run(["bash", "-c", "export"])
        run(["bash", "-c", "ls -la"])
        run(["bash", "-c", "ls -la .heroku"])
        run(["bash", "-c", "which npm"])
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
            run(["npm", "--proxy", os.environ["http_proxy"], "install", "--ignore-scripts"],
                cwd=os.path.join(install_path, "frontend"),
                shell=shell)
        else:
            printInfo("cd frontend")
            run(["npm", "install", "--ignore-scripts"], cwd=os.path.join(install_path, "frontend"),
                shell=shell)

        printInfo("cd frontend")
        # Circumvent bugs such as https://github.com/bower/bower/issues/646
        run(["bower", "cache", "clean"], cwd=os.path.join(install_path, "frontend"), shell=shell)
        run(["bower", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)

        if "frontend_gulp_build" in current_capabilities:
            printInfo("cd frontend")
            run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"), shell=shell)

        printSeparator()
        printInfo("Building online documentation")
        if isWindows:
            run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"), shell=True)
        else:
            run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)

    if "homepage_install" in current_capabilities:
        printSeparator()
        printInfo("Compiling homepage website")
        if "http_proxy" in os.environ:
            printNote("Behind a proxy: npm --proxy")
            printNote("You may want to add the following lines in your ~/.gitconfig:")
            printNote("   [url \"https://github.com\"]")
            printNote("      insteadOf=git://github.com")
            printInfo("cd homepage")
            run(["npm", "config", "set", "strict-ssl", "false"], cwd=os.path.join(install_path,
                                                                                  "homepage"),
                shell=shell)
            printInfo("cd homepage")
            run(["npm", "--proxy", os.environ["http_proxy"], "install", "--ignore-scripts"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)
        else:
            printInfo("cd homepage")
            run(["npm", "install", "--ignore-scripts"], cwd=os.path.join(install_path, "homepage"),
                shell=shell)

        printInfo("cd homepage")
        # Circumvent bugs such as https://github.com/bower/bower/issues/646
        run(["bower", "cache", "clean"], cwd=os.path.join(install_path, "homepage"), shell=shell)
        run(["bower", "install"], cwd=os.path.join(install_path, "homepage"), shell=shell)

        if "homepage_gulp_build" in current_capabilities:
            printInfo("cd homepage")
            run(["gulp", "build"], cwd=os.path.join(install_path, "homepage"), shell=shell)

        printSeparator()
        printInfo("Building online documentation")
        if isWindows:
            run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"), shell=True)
        else:
            run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)

    if "homepage_update" in current_capabilities:
        printInfo("Updating npm")
        printInfo("cd homepage")
        run(["npm", "install", "--save"],
            cwd=os.path.join(install_path, "homepage"),
            shell=shell)
        printInfo("Updating bower")
        printInfo("cd homepage")
        run(["bower", "install", "--save"],
            cwd=os.path.join(install_path, "homepage"),
            shell=shell)

    if "frontend_update" in current_capabilities:
        printInfo("Updating npm")
        printInfo("cd frontend")
        run(["npm", "install", "--save"],
            cwd=os.path.join(install_path, "frontend"),
            shell=shell)
        printInfo("Updating bower")
        printInfo("cd frontend")
        run(["bower", "install", "--save"],
            cwd=os.path.join(install_path, "frontend"),
            shell=shell)

    if "homepage_update_translations_fr" in current_capabilities:
        printInfo("Updating translation: Fr")
        printInfo("cd homepage")
        run(["poedit", os.path.join("src", "po", "fr.po")],
            cwd=os.path.join(install_path, "homepage"),
            shell=shell)

    if "frontend_update_translations_fr" in current_capabilities:
        printInfo("Updating translation: Fr")
        printInfo("cd frontend")
        run(["poedit", os.path.join("src", "po", "fr.po")],
            cwd=os.path.join(install_path, "frontend"),
            shell=shell)

    if "backend_test_unit" in current_capabilities:
        printSeparator()
        printInfo("Executing backend unit tests")
        run(["trial", "squirrel"],
            cwd=os.path.join(install_path, "backend"),
            shell=shell)

    if "backend_test_integration" in current_capabilities:
        printSeparator()
        printInfo("Executing backend integration tests")
        run(["trial", "squirrel_integration_tests"],
            cwd=os.path.join(install_path, "backend"),
            shell=shell)

    if "backend_update_translation" in current_capabilities:
        printSeparator()
        print("[INFO] Updating backend translation")
        run("xgettext --debug --language=Python --keyword=_ "
            "--output=po/Squirrel.pot $(find . -name '*.py')",
            cwd=os.path.join(install_path, "backend"), shell=True)

    if "serve_prod" in current_capabilities or "serve_staging" in current_capabilities:
        # Launching squirrel-prod
        server_base_name = "squirrel-prod"
        if "heroku" in current_capabilities:
            server_base_name = "squirrel-heroku"
        elif "serve_staging" in current_capabilities:
            server_base_name = "squirrel-staging"
        if isWindows:
            backend_launcher = os.path.join(workdir_path, "Scripts", server_base_name + ".exe")
        else:
            backend_launcher = server_base_name
        printInfo("Launching Prod Squirrel Server: {}".format(backend_launcher))

        run([backend_launcher])

    elif "serve_dev" in current_capabilities:
        # Launching squirrel-dev, which doesn't serve the front end, and let the front
        # be served by 'gulp serve'
        if isWindows:
            devbackend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-dev.exe")
        else:
            devbackend_launcher = "squirrel-dev"
        if "serve_dev_backend" in current_capabilities:
            printInfo("Launching squirrel-dev with auto relauncher {}".format(devbackend_launcher))
            sys.stdout.flush()
            sys.stderr.flush()

            sleep_sec = 0
            if isWindows:
                sleep_sec = 0

            auto_restart_backend_cmd = [
                "auto_relauncher", "--directory", "backend", "--recursive",
                "--sleep-between-restart", str(sleep_sec), "--patterns", "*.py;*.yaml",
                "--win32-safe-kill", "--verbose",
                devbackend_launcher]

            if ("serve_dev_frontend" in current_capabilities or
                    "serve_dev_homepage" in current_capabilities):
                run_background(auto_restart_backend_cmd, cwd=install_path)
            else:
                run(auto_restart_backend_cmd, cwd=install_path)
        if (("serve_dev_frontend" in current_capabilities or
                "serve_dev_homepage" in current_capabilities) and
                ("serve_dev_backend" in current_capabilities)):
            printInfo("Sleep 5 seconds")
            sys.stdout.flush()
            sys.stderr.flush()
            sleep(5)

        if "serve_dev_frontend" in current_capabilities:
            printInfo("Serving dev frontend")
            sleep_sec = 5

            auto_restart_backend_cmd = ["gulp", "serve"]

            run_background(auto_restart_backend_cmd,
                           cwd=os.path.join(install_path, "frontend"),
                           shell=shell)

        if "serve_dev_homepage" in current_capabilities:
            printInfo("Serving dev homepage")
            sleep_sec = 5

            auto_restart_backend_cmd = ["gulp", "serve"]

            run_background(auto_restart_backend_cmd,
                           cwd=os.path.join(install_path, "homepage"),
                           shell=shell)
        while True:
            printInfo(' -- Click Ctrl+C to close this window --')
            sleep(5)

    if "warn_no_serve_and_quit" in current_capabilities:
        printInfo("")
        printSeparator()
        printInfo("Do not start the server. Install is succesful.")
        if "novirtualenv" not in current_capabilities:
            printInfo("You can activate the virtualenv at the following path: {}"
                      .format(activate_path))
            if not isWindows:
                printInfo("(Use 'source activate' symbolic in your root folder)")
        printSeparator()
        sys.exit(0)
    else:
        printInfo("Done")
        printSeparator()
        sys.exit(0)

if __name__ == "__main__":
    main()
