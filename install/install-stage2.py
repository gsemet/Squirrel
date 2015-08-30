# This is the second part of the installation procedure or Squirrel.
# It should be executed from the virtualenv
# But beware, you might not have all the wonderful packages you will install with pip yet.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import imp
import os
import subprocess
import sys

from time import sleep

# Injecting available targets from installer stage 2
lib = imp.load_source('install-lib.py',
                      os.path.join(os.path.dirname(__file__), "install-lib.py"))


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
    "install:novirtualenv:frontend": "build/install only frontend without virtualenv (heroku model)",
    "install:novirtualenv:all":      "build/install all without virtualenv (heroku model)",
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
    "heroku:build:backend": "install:novirtualenv:backend",
    "heroku:build:all": "install:novirtualenv:all",
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
    "install:novirtualenv:backend": {
        "pip_upgrade",
        "backend_install",
        "novirtualenv",
        "warn_no_serve_and_quit",
    },
    "install:novirtualenv:all": {
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


def main():

    install_path = sys.argv[1]
    install_path = os.path.abspath(install_path)

    workdir_path = sys.argv[2]
    workdir_path = os.path.abspath(workdir_path)

    subcmd = sys.argv[3]

    lib.printSeparator("=")
    lib.printInfo("Squirrel Installer Stage 2")
    if subcmd not in cmd_capabilities.keys():
        lib.printError("Invalid install target: {}. Available: {}"
                       .format(subcmd, cmd_capabilities.keys()))
        sys.exit(1)
    current_capabilities = cmd_capabilities[subcmd]
    if "help" in current_capabilities:
        lib.printInfo("Help")
        return 0
    if "VIRTUAL_ENV" not in os.environ:
        lib.printInfo("We are **NOT** in a virtualenv")
    else:
        lib.printInfo("We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
    lib.printInfo("Interpreter: {0} - Version: {1}".format(sys.executable,
                                                           sys.version.split("\n")[0]))
    lib.printInfo("installation dir: {}".format(install_path))
    lib.printInfo("workdir: {}".format(workdir_path))
    lib.printInfo("Executing command: '{}'".format(subcmd))
    lib.printInfo("Install Capabilities: {}".format(", ".join(sorted(list(current_capabilities)))))
    lib.printInfo("Environment variables:")
    for k, v in sorted(os.environ.items()):
        lib.printInfo("  {0}:{1}".format(k, v))

    lib.printSeparator("=")
    lib.printInfo("")
    lib.printInfo("Installation process really starts here...")
    lib.printInfo("")

    if lib.isWindows:
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
                lib.printSeparator()
                lib.printInfo("Patching this pip (version) {}.{}), "
                              "to fix proxy issue (fixed in pip 1.6)"
                              .format(pip_major, pip_minor))
                lib.printInfo("See: https://github.com/pypa/pip/issues/1805")
                # Patching the installed pip to fix the following bug with proxy
                # See http://www.irvingc.com/posts/10
                patch_path = os.path.join(install_path, "install", "patch-pip.patch")
                c = call(["bash", "-c", "patch -p0 -N --dry-run --silent < {} 2>/dev/null"
                          .format(patch_path)])
                if not c:
                    lib.printInfo("Applying patch")
                    lib.run(["bash", "-c", "patch -p0 < {}".format(patch_path)])
                else:
                    lib.printInfo("Already applied. Skipping patch")

        lib.printSeparator()
        lib.printInfo("Updating pip (try to always use latest version of pip)")
        lib.printInfo("cd backend")
        lib.run(["pip", "install", "--upgrade", "pip"])

    if "backend_install" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Installing backend requirements")
        lib.printInfo("cd backend")
        lib.run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                                      "requirements.txt")])

        if sys.version_info < (3, 4):
            lib.printInfo("Python version {}.{} < 3.4, installing extra requirements"
                          .format(sys.version_info[0], sys.version_info[2]))
            lib.printInfo("cd backend")
            lib.run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                                          "requirements-py_lt34.txt")])

        if lib.isWindows:
            lib.printSeparator()
            lib.printInfo("Installing Windows dependencies")
            lib.run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                                          "requirements-win32.txt")])
            lib.printInfo("Ensure you have win32api installed")

        lib.printSeparator()
        lib.printInfo("Installing backend")
        lib.printInfo("cd backend")
        lib.run(["pip", "install", "-e", os.path.join(install_path, "backend")])

    if "frontend_install" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Compiling frontend website")
        lib.printInfo("PWD")
        lib.run_nocheck(["bash", "-c", "echo PWD=$PWD"])
        lib.run_nocheck(["bash", "-c", "echo PATH=$PATH"])
        lib.run_nocheck(["bash", "-c", "export"])
        lib.run_nocheck(["bash", "-c", "ls -la"])
        lib.run_nocheck(["bash", "-c", "ls -la .heroku"])
        lib.run_nocheck(["bash", "-c", "which npm"])
        if "http_proxy" in os.environ:
            printNote("Behind a proxy: npm --proxy")
            printNote("You may want to add the following lines in your ~/.gitconfig:")
            printNote("   [url \"https://github.com\"]")
            printNote("      insteadOf=git://github.com")
            lib.printInfo("cd frontend")
            lib.run(["npm", "config", "set", "strict-ssl", "false"],
                    cwd=os.path.join(install_path,
                                     "frontend"),
                    shell=shell)
            lib.printInfo("cd frontend")
            lib.run(["npm", "--proxy", os.environ["http_proxy"], "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "frontend"),
                    shell=shell)
        else:
            lib.printInfo("cd frontend")
            lib.run(["npm", "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "frontend"),
                    shell=shell)

        lib.printInfo("cd frontend")
        # Circumvent bugs such as https://github.com/bower/bower/issues/646
        lib.run(["bower", "cache", "clean"], cwd=os.path.join(install_path, "frontend"),
                shell=shell)
        lib.run(["bower", "install"], cwd=os.path.join(install_path, "frontend"),
                shell=shell)

        if "frontend_gulp_build" in current_capabilities:
            lib.printInfo("cd frontend")
            lib.run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"),
                    shell=shell)

        lib.printSeparator()
        lib.printInfo("Building online documentation")
        if lib.isWindows:
            lib.run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"),
                    shell=True)
        else:
            lib.run(["make", "html"], cwd=os.path.join(install_path, "doc"),
                    shell=shell)

    if "homepage_install" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Compiling homepage website")
        if "http_proxy" in os.environ:
            printNote("Behind a proxy: npm --proxy")
            printNote("You may want to add the following lines in your ~/.gitconfig:")
            printNote("   [url \"https://github.com\"]")
            printNote("      insteadOf=git://github.com")
            lib.printInfo("cd homepage")
            lib.run(["npm", "config", "set", "strict-ssl", "false"], cwd=os.path.join(install_path,
                                                                                      "homepage"),
                    shell=shell)
            lib.printInfo("cd homepage")
            lib.run(["npm", "--proxy", os.environ["http_proxy"], "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "homepage"),
                    shell=shell)
        else:
            lib.printInfo("cd homepage")
            lib.run(["npm", "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "homepage"),
                    shell=shell)

        lib.printInfo("cd homepage")
        # Circumvent bugs such as https://github.com/bower/bower/issues/646
        lib.run(["bower", "cache", "clean"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)
        lib.run(["bower", "install"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)

        if "homepage_gulp_build" in current_capabilities:
            lib.printInfo("cd homepage")
            lib.run(["gulp", "build"],
                    cwd=os.path.join(install_path, "homepage"),
                    shell=shell)

        lib.printSeparator()
        lib.printInfo("Building online documentation")
        if lib.isWindows:
            lib.run(["make.bat", "html"],
                    cwd=os.path.join(install_path, "doc"),
                    shell=True)
        else:
            lib.run(["make", "html"],
                    cwd=os.path.join(install_path, "doc"),
                    shell=shell)

    if "homepage_update" in current_capabilities:
        lib.printInfo("Updating npm")
        lib.printInfo("cd homepage")
        lib.run(["npm", "install", "--save"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)
        lib.printInfo("Updating bower")
        lib.printInfo("cd homepage")
        lib.run(["bower", "install", "--save"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)

    if "frontend_update" in current_capabilities:
        lib.printInfo("Updating npm")
        lib.printInfo("cd frontend")
        lib.run(["npm", "install", "--save"],
                cwd=os.path.join(install_path, "frontend"),
                shell=shell)
        lib.printInfo("Updating bower")
        lib.printInfo("cd frontend")
        lib.run(["bower", "install", "--save"],
                cwd=os.path.join(install_path, "frontend"),
                shell=shell)

    if "homepage_update_translations_fr" in current_capabilities:
        lib.printInfo("Updating translation: Fr")
        lib.printInfo("cd homepage")
        lib.run(["poedit", os.path.join("src", "po", "fr.po")],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)

    if "frontend_update_translations_fr" in current_capabilities:
        lib.printInfo("Updating translation: Fr")
        lib.printInfo("cd frontend")
        lib.run(["poedit", os.path.join("src", "po", "fr.po")],
                cwd=os.path.join(install_path, "frontend"),
                shell=shell)

    if "backend_test_unit" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Executing backend unit tests")
        lib.run(["trial", "squirrel"],
                cwd=os.path.join(install_path, "backend"),
                shell=shell)

    if "backend_test_integration" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Executing backend integration tests")
        lib.run(["trial", "squirrel_integration_tests"],
                cwd=os.path.join(install_path, "backend"),
                shell=shell)

    if "backend_update_translation" in current_capabilities:
        lib.printSeparator()
        print("[INFO] Updating backend translation")
        lib.run("xgettext --debug --language=Python --keyword=_ "
                "--output=po/Squirrel.pot $(find . -name '*.py')",
                cwd=os.path.join(install_path, "backend"), shell=True)

    if "serve_prod" in current_capabilities or "serve_staging" in current_capabilities:
        # Launching squirrel-prod
        server_base_name = "squirrel-prod"
        if "heroku" in current_capabilities:
            server_base_name = "squirrel-heroku"
        elif "serve_staging" in current_capabilities:
            server_base_name = "squirrel-staging"
        if lib.isWindows:
            backend_launcher = os.path.join(workdir_path, "Scripts", server_base_name + ".exe")
        else:
            backend_launcher = server_base_name
        lib.printInfo("Launching Prod Squirrel Server: {}".format(backend_launcher))

        lib.run([backend_launcher])

    elif "serve_dev" in current_capabilities:
        # Launching squirrel-dev, which doesn't serve the front end, and let the front
        # be served by 'gulp serve'
        if lib.isWindows:
            devbackend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-dev.exe")
        else:
            devbackend_launcher = "squirrel-dev"
        if "serve_dev_backend" in current_capabilities:
            lib.printInfo("Launching squirrel-dev with auto relauncher {}"
                          .format(devbackend_launcher))
            sys.stdout.flush()
            sys.stderr.flush()

            sleep_sec = 0
            if lib.isWindows:
                sleep_sec = 0

            auto_restart_backend_cmd = [
                "auto_relauncher", "--directory", "backend", "--recursive",
                "--sleep-between-restart", str(sleep_sec), "--patterns", "*.py;*.yaml",
                "--win32-safe-kill", "--verbose",
                devbackend_launcher]

            if ("serve_dev_frontend" in current_capabilities or
                    "serve_dev_homepage" in current_capabilities):
                lib.run_background(auto_restart_backend_cmd, cwd=install_path)
            else:
                lib.run(auto_restart_backend_cmd, cwd=install_path)
        if (("serve_dev_frontend" in current_capabilities or
                "serve_dev_homepage" in current_capabilities) and
                ("serve_dev_backend" in current_capabilities)):
            lib.printInfo("Sleep 5 seconds")
            sys.stdout.flush()
            sys.stderr.flush()
            sleep(5)

        if "serve_dev_frontend" in current_capabilities:
            lib.printInfo("Serving dev frontend")
            sleep_sec = 5

            auto_restart_backend_cmd = ["gulp", "serve"]

            lib.run_background(auto_restart_backend_cmd,
                               cwd=os.path.join(install_path, "frontend"),
                               shell=shell)

        if "serve_dev_homepage" in current_capabilities:
            lib.printInfo("Serving dev homepage")
            sleep_sec = 5

            auto_restart_backend_cmd = ["gulp", "serve"]

            lib.run_background(auto_restart_backend_cmd,
                               cwd=os.path.join(install_path, "homepage"),
                               shell=shell)
        while True:
            lib.printInfo(' -- Click Ctrl+C to close this window --')
            sleep(5)

    if "warn_no_serve_and_quit" in current_capabilities:
        lib.printInfo("")
        lib.printSeparator()
        lib.printInfo("Do not start the server. Install is succesful.")
        if "novirtualenv" not in current_capabilities:
            lib.printInfo("You can activate the virtualenv at the following path: {}"
                          .format(activate_path))
            if not lib.isWindows:
                lib.printInfo("(Use 'source activate' symbolic in your root folder)")
        lib.printSeparator()
        sys.exit(0)
    else:
        lib.printInfo("Done")
        lib.printSeparator()
        sys.exit(0)

if __name__ == "__main__":
    main()
