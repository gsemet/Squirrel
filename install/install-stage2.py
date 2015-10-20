# This is the second part of the installation procedure or Squirrel.
# It should be executed from the virtualenv
# But beware, you might not have all the wonderful packages you will install with pip yet.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import imp
import json
import os
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
    "install:all":              "build/install backend, frontend and homepage",
    "install:all-clean":        "build/install backend, frontend and homepage, then clean build",
    "install:novirtualenv:backend": "build/install only backend without virtualenv (heroku model)",
    "install:novirtualenv:all":     "build/install all without virtualenv (heroku model)",
    "update:all":              ("update all dependencies (modules installed by npm and bower) "
                                "and translations"),
    "update:lang:all":          "update all translations files - requires 'poedit'",
    "update:lang:en":           "update translation (en) - requires 'poedit'",
    "update:lang:fr":           "update translation (fr) - requires 'poedit'",
    "test:all":                ("execute all tests (unit tests, integration tests, e2e tests)"),
    "test:unit":               ("execute all unit tests"),
    "test:integration":        ("execute all integration tests (which depends on external systems)"),
    "test:e2e":                ("execute end to end tests"),
    "update:node:base":        ("install and update node (require root password)"),
    "update:node:list":        ("list version of all your package to latest version"),
    "update:node:package":     ("update all your 'package.json' dependencies to latest version"),
    "update:node:bower":       ("update all your 'bower.json' dependencies to latest version"),
    "update:pip:all":          ("update pip's 'requirements.txt' dependencies to latest version"),
}
aliases = {
    "(empty)": "install:all",
    "serve": "serve:dev",
    "serve:homepage": "serve:dev:homepage",
    "serve:frontend": "serve:dev:frontend",
    "serve:backend": "serve:dev:backend",
    "dev": "serve:dev",
    "dev:backend": "serve:dev:backend",
    "dev:homepage": "serve:dev:homepage",
    "dev:frontend": "serve:dev:frontend",
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
        "check_dependencies",
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "build_homepage",
        "build_doc",
        "serve",
        "serve_dev",
        "serve_dev_backend",
        "serve_dev_frontend",
        "serve_dev_homepage",
        "start_mongo_if_needed",
    },
    "serve:dev:backend": {
        "check_dependencies",
        "pip_upgrade",
        "build_install",
        "serve",
        "serve_dev",
        "serve_dev_backend",
        "start_mongo_if_needed",
    },
    "serve:dev:frontend": {
        "build_frontend",
        "serve",
        "serve_dev",
        "serve_dev_frontend",
    },
    "serve:dev:homepage": {
        "build_homepage",
        "serve",
        "serve_dev",
        "serve_dev_homepage",
    },
    "serve:prod": {
        "check_dependencies",
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "build_homepage",
        "build_doc",
        "frontend_gulp_build",
        "homepage_gulp_build",
        "serve",
        "serve_prod",
        "start_mongo_if_needed",
    },
    "serve:staging": {
        "check_dependencies",
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "build_doc",
        "frontend_gulp_build",
        "build_homepage",
        "homepage_gulp_build",
        "serve",
        "serve_staging",
        "start_mongo_if_needed",
    },
    "serve:novirtualenv": {
        "check_dependencies",
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "build_doc",
        "frontend_gulp_build",
        "build_homepage",
        "homepage_gulp_build",
        "serve",
        "serve_prod",
        "start_mongo_if_needed",
        "novirtualenv",
        "heroku",
    },
    "start:prod": {
        "serve",
        "serve_prod",
        "start_mongo_if_needed",
    },
    "start:staging": {
        "serve",
        "serve_staging",
    },
    "start:dev": {
        "serve",
        "serve_dev",
        "start_mongo_if_needed",
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
        "start_mongo_if_needed",
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
        "build_install",
        "build_frontend",
        "build_homepage",
        "build_doc",
        "frontend_gulp_build",
        "homepage_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:all-clean": {
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "build_homepage",
        "build_doc",
        "clean_prod",
        "frontend_gulp_build",
        "homepage_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:backend": {
        "pip_upgrade",
        "build_install",
        "warn_no_serve_and_quit",
    },
    "install:frontend": {
        "build_frontend",
        "frontend_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:homepage": {
        "build_homepage",
        "homepage_gulp_build",
        "warn_no_serve_and_quit",
    },
    "install:novirtualenv:backend": {
        "pip_upgrade",
        "build_install",
        "novirtualenv",
        "warn_no_serve_and_quit",
    },
    "install:novirtualenv:all": {
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "build_homepage",
        "novirtualenv",
        "warn_no_serve_and_quit",
    },
    'update:all': {
        "pip_upgrade",
        "build_install",
        "build_frontend",
        "frontend_update",
        "frontend_update_npm",
        "frontend_update_bower",
        "frontend_gulp_build",
        "frontend_update_translations_fr",
        "frontend_update_translations_en",
        "build_homepage",
        "build_doc",
        "homepage_update",
        "homepage_update_npm",
        "homepage_update_bower",
        "homepage_gulp_build",
        "homepage_update_translations_fr"
        "homepage_update_translations_en"
    },
    'update:lang:all': {
        "pip_upgrade",
        "build_install",
        "backend_update_translation",
        "build_frontend",
        "frontend_gulp_build",
        "frontend_update_translations_fr",
        "frontend_update_translations_en",
        "build_homepage",
        "homepage_gulp_build",
        "homepage_update_translations_fr",
        "homepage_update_translations_en",
        # add all update cap here
    },
    'update:lang:fr': {
        "pip_upgrade",
        "build_install",
        "backend_update_translation",
        "build_frontend",
        "frontend_gulp_build",
        "frontend_update_translations_fr",
        "build_homepage",
        "homepage_gulp_build",
        "homepage_update_translations_fr",
    },
    'update:lang:en': {
        "pip_upgrade",
        "build_install",
        "backend_update_translation",
        "build_frontend",
        "frontend_gulp_build",
        "frontend_update_translations_en",
        "build_homepage",
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
    "update:node:base": {
        "update_node_base",
    },
    "update:node:list": {
        "update_node_list",
    },
    "update:node:package": {
        "update_node_package",
    },
    "update:node:bower": {
        "update_node_bower",
    },
    "update:pip:all": {
        "update_pip_all",
    },
}


def main():

    install_path = sys.argv[1]
    install_path = os.path.abspath(install_path)

    workdir_path = sys.argv[2]
    workdir_path = os.path.abspath(workdir_path)

    subcmd = sys.argv[3]

    if not lib.isWindows:
        pip_exe = "pip"
    else:
        pip_exe = "pip.exe"

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
    lib.printInfo("PATH: {}".format(os.environ['PATH']))
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

    environ_json_path = os.path.join(workdir_path, "environ.json")
    json_read_environ = {}
    if os.path.exists(environ_json_path):
        lib.printSeparator()
        lib.printInfo("Environment variable json file found, sourcing it from {}"
                      .format(environ_json_path))
        with open(environ_json_path) as f:
            content = f.read()
            lib.printDebug("content: {!r}".format(content))
            if content:
                environ_json = json.loads(content)
                for name, var in environ_json.items():
                    lib.printInfo("  {}={}".format(name, var))
                    os.environ[name] = var
                    json_read_environ[name] = var
        if not content:
            lib.printInfo("Removing {} because it is empty".format(environ_json_path))
            os.unlink(environ_json_path)

    if "update_node_base" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Updating our lovely node tools:")
        lib.printInfo(" - bower")
        lib.printInfo(" - gulp")
        lib.printInfo(" - grunt")
        lib.printInfo(" - npm-check-updates")
        lib.printInfo(" - bower-update")
        lib.printInfo("...")

        if "http_proxy" in os.environ:
            lib.printNote("Behind a proxy: npm --proxy")
            npm_base_cmd = ["npm", "--proxy", os.environ["http_proxy"]]
        else:
            npm_base_cmd = ["npm"]

        try:
            lib.run(npm_base_cmd + ["install", "-g", "bower"])
        except:
            lib.printInfo("Install failed, trying with sudo")
            lib.run(["sudo", "-E"] + npm_base_cmd + ["install", "-g", "bower"])
        try:
            lib.run(npm_base_cmd + ["install", "-g", "gulp"])
        except:
            lib.printInfo("Install failed, trying with sudo")
            lib.run(["sudo", "-E"] + npm_base_cmd + ["install", "-g", "gulp"])
        try:
            lib.run(npm_base_cmd + ["install", "-g", "grunt"])
        except:
            lib.printInfo("Install failed, trying with sudo")
            lib.run(["sudo", "-E"] + npm_base_cmd + ["install", "-g", "grunt"])
        try:
            lib.run(npm_base_cmd + ["install", "-g", "npm-check-updates"])
        except:
            lib.printInfo("Install failed, trying with sudo")
            lib.run(["sudo", "-E"] + npm_base_cmd + ["install", "-g", "npm-check-updates"])
        try:
            lib.run(npm_base_cmd + ["install", "-g", "bower-update"])
        except:
            lib.printInfo("Install failed, trying with sudo")
            lib.run(["sudo", "-E"] + npm_base_cmd + ["install", "-g", "bower-update"])

    if "update_node_list" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Running the great 'ncu' tool.")
        lib.printInfo("Please wait it may take some times...")
        lib.printCmd("cd homepage")
        lib.run(["ncu"],
                cwd=os.path.join(install_path,
                                 "homepage"),
                shell=shell)
        lib.printCmd("cd frontend")
        lib.run(["ncu"],
                cwd=os.path.join(install_path,
                                 "frontend"),
                shell=shell)

    if "update_node_package" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Updating all 'package.json' with the greatest 'ncu' tool.")
        lib.printInfo("Please wait it may take some times...")
        lib.printCmd("cd homepage")
        lib.run(["ncu", "-u"],
                cwd=os.path.join(install_path,
                                 "homepage"),
                shell=shell)
        lib.printCmd("cd frontend")
        lib.run(["ncu", "-u"],
                cwd=os.path.join(install_path,
                                 "frontend"),
                shell=shell)

    if "update_node_bower" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Updating all 'bower.json' with the greatest 'bower-update' tool.")
        lib.printInfo("Please wait it may take some times...")
        lib.printCmd("cd homepage")
        lib.run(["bower-update"],
                cwd=os.path.join(install_path,
                                 "homepage"),
                shell=shell)
        lib.printCmd("cd frontend")
        lib.run(["bower-update"],
                cwd=os.path.join(install_path,
                                 "frontend"),
                shell=shell)

    if "update_pip_all" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Updating 'requirements' with the greatest 'pip-tools' tool.")
        lib.printInfo("Please wait it may take some times...")
        lib.printCmd("cd backend")
        lib.run(["pip-compile"],
                cwd=os.path.join(install_path,
                                 "backend"),
                shell=shell)
        lib.run(["pip-sync"],
                cwd=os.path.join(install_path,
                                 "backend"),
                shell=shell)

    if "check_dependencies" in current_capabilities:
        user_env_var = {}
        lib.printSeparator()
        lib.printInfo("External dependency check is required")
        if os.environ.get('MONGO_DB_URL'):
            lib.printInfo("Using MONGO_DB_URL={}".format(os.environ.get('MONGO_DB_URL')))
        else:
            lib.printInfo("MONGO_DB_URL environment variable not found")
            if os.environ.get("MONGOD_PATH"):
                lib.printInfo("Using MONGOD_PATH={}".format(os.environ.get('MONGOD_PATH')))
            else:
                lib.printInfo("MONGOD_PATH environment variable not set")
                mongod_path = None
                if not lib.isWindows:
                    try:
                        mongod_path = lib.run_output(["which", "mongod"])
                        mongod_path = mongod_path.strip()
                    except:
                        mongod_path = None
                res = lib.printQuestion("Do you want to manage MongoDB server?\n"
                                        "1 = Let Squirrel Installer start/stop MongoDB server "
                                        "(mongod)\n"
                                        "2 = MongoDB daemon (mongod) is already running, just "
                                        "set the URL")
                if res == "1":
                    if mongod_path:
                        lib.printInfo("'mongod' found: {}".format(mongod_path))
                        user_env_var["MONGOD_PATH"] = mongod_path
                    else:
                        res = lib.printQuestion("Where MongoDB is installed (path to 'mongod{}')?"
                                                .format(".exe" if lib.isWindows else ""))
                        if not os.path.exists(os.path.abspath(res)):
                            lib.printError("Path does not exist: {}".format(res))
                            return 1
                        user_env_var["MONGOD_PATH"] = res
                elif res == "2":
                    res = lib.printQuestion("What is the URL of your MongoDB server "
                                            "(empty='localhost:27017') ?")
                    res = res.split()
                    if not res:
                        res = 'localhost:27017'
                    user_env_var["MONGO_DB_URL"] = res
                    lib.printInfo("Setting MONGO_DB_URL to '{}'".format(res))
                else:
                    lib.printError("Invalid anwser: {}".format(res))
                    return 1

        if os.environ.get('DATABASE_URL'):
            lib.printInfo("Using DATABASE_URL={}".format(os.environ.get('DATABASE_URL')))
        else:
            lib.printInfo("DATABASE_URL environment variable not found")
            res = lib.printQuestion("What is the URL of your PostgreSQL server "
                                    "(empty='localhost:5432') ?")
            res = res.split()
            if not res:
                res = 'localhost:5432'
            user_env_var["DATABASE_URL"] = res
            lib.printInfo("Setting DATABASE_URL to '{}'".format(res))

        if user_env_var:
            lib.printInfo("Writing environment json: {}".format(environ_json_path))
            with open(environ_json_path, "w") as f:
                res = user_env_var.copy()
                res.update(json_read_environ)
                f.writelines(json.dumps(res,
                                        sort_keys=True,
                                        indent=4,
                                        separators=(',', ': ')))
            for name, var in user_env_var.items():
                os.environ[name] = var

    if "check_dependencies" in current_capabilities:
        lib.printInfo("Checking mandatory dependencies: ")
        lib.printInfo(" - virtualenv")  # (already checked in stage1)
        lib.printInfo(" - pip")
        lib.printInfo(" - MongoDB")
        lib.printInfo(" - PostgreSQL")
        # macos: homebrew/port
        lib.printInfo(" - node")
        # find nodejs on debian and warn to install manually the node package from node.io!
        lib.printInfo(" - bower")
        lib.printInfo("OK")

    if "pip_upgrade" in current_capabilities:
        lib.printInfo("Updating pip (try to always use latest version of pip)")
        lib.run([pip_exe, "install", "--upgrade", "pip"])

        lib.printSeparator()

        if sys.platform.startswith("linux"):
            pip_version_str = lib.run_output([pip_exe, "--version"])
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
                c = lib.call(["bash", "-c", "patch -p0 -N --dry-run --silent < {} 2>/dev/null"
                              .format(patch_path)])
                if not c:
                    lib.printInfo("Applying patch")
                    lib.run(["bash", "-c", "patch -p0 < {}".format(patch_path)])
                else:
                    lib.printInfo("Already applied. Skipping patch")

    if "build_install" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Installing backend requirements")
        lib.printCmd("cd backend")
        lib.run([pip_exe, "install", "-r", os.path.join(install_path, "backend",
                                                        "requirements.txt")])

        if sys.version_info < (3, 4):
            lib.printInfo("Python version {}.{} < 3.4, installing extra requirements"
                          .format(sys.version_info[0], sys.version_info[2]))
            lib.printCmd("cd backend")
            lib.run([pip_exe, "install", "-r", os.path.join(install_path, "backend",
                                                            "requirements-py_lt34.txt")])

        if lib.isWindows:
            lib.printSeparator()
            lib.printInfo("Installing Windows dependencies")
            lib.run([pip_exe, "install", "-r", os.path.join(install_path, "backend",
                                                            "requirements-win32.txt")])
            lib.printInfo("Ensure you have win32api installed")

        lib.printSeparator()
        lib.printInfo("Installing backend")
        lib.printCmd("cd backend")
        lib.run([pip_exe, "install", "-e", os.path.join(install_path, "backend")])

    if "build_frontend" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Compiling frontend website")
        if "http_proxy" in os.environ:
            lib.printNote("Behind a proxy: npm --proxy")
            lib.printNote("You may want to add the following lines in your ~/.gitconfig:")
            lib.printNote("   [url \"https://github.com\"]")
            lib.printNote("      insteadOf=git://github.com")
            lib.printCmd("cd frontend")
            lib.run(["npm", "config", "set", "strict-ssl", "false"],
                    cwd=os.path.join(install_path,
                                     "frontend"),
                    shell=shell)
            lib.printCmd("cd frontend")
            lib.run(["npm", "--proxy", os.environ["http_proxy"], "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "frontend"),
                    shell=shell)
        else:
            lib.printCmd("cd frontend")
            lib.run(["npm", "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "frontend"),
                    shell=shell)

        lib.printCmd("cd frontend")
        # Circumvent bugs such as https://github.com/bower/bower/issues/646
        lib.run(["bower", "cache", "clean", "--allow-root"], cwd=os.path.join(install_path,
                                                                              "frontend"),
                extraPath=os.path.join(install_path, "frontend", "node_modules", ".bin"),
                shell=shell)
        lib.run(["bower", "install", "--allow-root"], cwd=os.path.join(install_path, "frontend"),
                extraPath=os.path.join(install_path, "frontend", "node_modules", ".bin"),
                shell=shell)

        if "frontend_gulp_build" in current_capabilities:
            lib.printCmd("cd frontend")
            lib.run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"),
                    extraPath=os.path.join(install_path, "frontend", "node_modules", ".bin"),
                    shell=shell)

    if "build_homepage" in current_capabilities:
        lib.printSeparator()
        lib.printInfo("Compiling homepage website")
        if "http_proxy" in os.environ:
            lib.printNote("Behind a proxy: npm --proxy")
            lib.printNote("You may want to add the following lines in your ~/.gitconfig:")
            lib.printNote("   [url \"https://github.com\"]")
            lib.printNote("      insteadOf=git://github.com")
            lib.printCmd("cd homepage")
            lib.run(["npm", "config", "set", "strict-ssl", "false"], cwd=os.path.join(install_path,
                                                                                      "homepage"),
                    shell=shell)
            lib.printCmd("cd homepage")
            lib.run(["npm", "--proxy", os.environ["http_proxy"], "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "homepage"),
                    shell=shell)
        else:
            lib.printCmd("cd homepage")
            lib.run(["npm", "install", "--ignore-scripts"],
                    cwd=os.path.join(install_path, "homepage"),
                    shell=shell)

        lib.printCmd("cd homepage")
        # Circumvent bugs such as https://github.com/bower/bower/issues/646
        lib.run(["bower", "cache", "clean", "--allow-root"],
                cwd=os.path.join(install_path, "homepage"),
                extraPath=os.path.join(install_path, "homepage", "node_modules", ".bin"),
                shell=shell)
        lib.run(["bower", "install", "--allow-root"],
                cwd=os.path.join(install_path, "homepage"),
                extraPath=os.path.join(install_path, "homepage", "node_modules", ".bin"),
                shell=shell)

        if "homepage_gulp_build" in current_capabilities:
            lib.printCmd("cd homepage")
            lib.run(["gulp", "build"],
                    cwd=os.path.join(install_path, "homepage"),
                    extraPath=os.path.join(install_path, "homepage", "node_modules", ".bin"),
                    shell=shell)

    if "build_doc" in current_capabilities:
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
        lib.printCmd("cd homepage")
        lib.run(["npm", "install", "--save"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)
        lib.printInfo("Updating bower")
        lib.printCmd("cd homepage")
        lib.run(["bower", "install", "--save"],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)

    if "frontend_update" in current_capabilities:
        lib.printInfo("Updating npm")
        lib.printCmd("cd frontend")
        lib.run(["npm", "install", "--save"],
                cwd=os.path.join(install_path, "frontend"),
                shell=shell)
        lib.printInfo("Updating bower")
        lib.printCmd("cd frontend")
        lib.run(["bower", "install", "--save"],
                cwd=os.path.join(install_path, "frontend"),
                extraPath=os.path.join(install_path, "frontend", "node_modules", ".bin"),
                shell=shell)

    if "homepage_update_translations_fr" in current_capabilities:
        lib.printInfo("Updating translation: Fr")
        lib.printCmd("cd homepage")
        lib.run(["poedit", os.path.join("src", "po", "fr.po")],
                cwd=os.path.join(install_path, "homepage"),
                shell=shell)

    if "frontend_update_translations_fr" in current_capabilities:
        lib.printInfo("Updating translation: Fr")
        lib.printCmd("cd frontend")
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
        lib.printInfo("Updating backend translation")
        lib.run("xgettext --debug --language=Python --keyword=_ "
                "--output=po/Squirrel.pot $(find . -name '*.py')",
                cwd=os.path.join(install_path, "backend"), shell=True)

    if "start_mongo_if_needed" in current_capabilities:
        if os.environ.get("MONGOD_PATH"):
            lib.printInfo("Starting mongod: {}".format(os.environ["MONGOD_PATH"]))
            mongo_dbpath = os.path.join(workdir_path, "mongodb")
            lib.mkdirs(mongo_dbpath)
            lib.run_background([os.environ["MONGOD_PATH"], "--dbpath", mongo_dbpath])
            os.environ["MONGO_DB_URL"] = "localhost:27017"
        else:
            lib.printInfo("Do not start MongoDB")

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

    if "clean_prod" in current_capabilities:
        lib.run_background([os.path.join("install", "uninstall.py"), "--no-dist"],
                           shell=shell)

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
