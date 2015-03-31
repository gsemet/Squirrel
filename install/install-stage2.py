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

do_launch = sys.argv[3]

if not os.environ['VIRTUAL_ENV']:
    raise Exception("VIRTUAL_ENV environment variable is empty. We are not in a virtualenv.")

print("===============================================================================")
print("[INFO] Squirrel Installer Stage 2")
print("[INFO] We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
print("[INFO] Interpreter: {0} - Version: {1}".format(sys.executable, sys.version.split("\n")[0]))
print("[INFO] installation dir: {}".format(install_path))
print("[INFO] workdir: {}".format(workdir_path))
print("[INFO] Launch: {}".format(do_launch))
print("[INFO] Environment variables:")
for k, v in sorted(os.environ.items()):
    print("[INFO]   {0}:{1}".format(k, v))

print("===============================================================================")
print("[INFO] ")
print("[INFO] Installation really starts...")
print("[INFO] ")


def run(cmd, cwd=None, shell=False):
    print("[CMD ] {}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def call(cmd, cwd=None, shell=False):
    print("[CMD ] {}".format(" ".join(cmd)))
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def run_background(cmd, cwd=None, shell=False):
    print("[CMD (background)] {}".format(" ".join(cmd)))
    subprocess.Popen(cmd, cwd=cwd, shell=shell)


if sys.platform.startswith("linux"):
    print("-------------------------------------------------------------------------------")
    pip_version_str = subprocess.check_output(["pip", "--versio"])
    pip_version_str = pip_version_str.split(" ")[1]
    pip_version_str = pip_version_str.split("-")[0]
    pip_version_str = pip_version_str.split("_")[0]
    pip_version_str = pip_version_str.rpartition(".")[0]
    pip_major, _, pip_minor = pip_version_str.partition(".")
    pip_version = int(pip_major) * 100 + int(pip_minor)
    if pip_version <= 105:
        print("[INFO] Patching this pip (version) {}.{}), to fix proxy issue (fixed in pip 1.6)"
              .format(pip_major, pip_minor))
        print("[INFO] See: https://github.com/pypa/pip/issues/1805")
        # Patching the installed pip to fix the following bug with proxy
        # See http://www.irvingc.com/posts/10
        patch_path = os.path.join(install_path, "install", "patch-pip.patch")
        c = call(["bash", "-c", "patch -p0 -N --dry-run --silent < {} 2>/dev/null"
                  .format(patch_path)])
        if not c:
            print("[INFO] Applying patch")
            run(["bash", "-c", "patch -p0 < {}".format(patch_path)])
        else:
            print("[INFO] Already applied. Skipping patch")

print("-------------------------------------------------------------------------------")
print("[INFO] Installing backend requirements")
print("[INFO] cd backend")
run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                          "requirements.txt")])

if sys.platform.startswith('win32'):
    print("-------------------------------------------------------------------------------")
    print("[INFO] Installing Windows dependencies")
    run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                              "requirements-win32.txt")])
    print("[INFO] Ensure you have win32api installed")


print("-------------------------------------------------------------------------------")
print("[INFO] Installing backend")
print("[INFO] cd backend")
run(["pip", "install", "-e", os.path.join(install_path, "backend")])

if sys.platform.startswith('win32'):
    shell = True
else:
    shell = False

if do_launch != "install_only_backend":
    print("-------------------------------------------------------------------------------")
    print("[INFO] Compiling frontend website")
    if "http_proxy" in os.environ:
        print("[INFO] Behind a proxy: npm --proxy")
        print("[INFO] cd frontend")
        run(["npm", "config", "set", "strict-ssl", "false"], cwd=os.path.join(install_path,
                                                                              "frontend"),
            shell=shell)
        print("[INFO] cd frontend")
        run(["npm", "--proxy", os.environ["http_proxy"], "install"], cwd=os.path.join(install_path,
                                                                                      "frontend"),
            shell=shell)
    else:
        print("[INFO] cd frontend")
        run(["npm", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    print("[INFO] cd frontend")
    run(["bower", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    if do_launch != "dev-server":
        print("[INFO] cd frontend")
        run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"), shell=shell)

    print("-------------------------------------------------------------------------------")
    print("[INFO] Building online documentation")
    if sys.platform.startswith('win32'):
        run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"), shell=True)
    else:
        run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)

if do_launch == "only_install":
    print("")
    print("-------------------------------------------------------------------------------")
    print("Do not start the server. Install is succesful.")
    print("-------------------------------------------------------------------------------")
    sys.exit(0)

print("-------------------------------------------------------------------------------")
if do_launch == "server":
    # Launching Squirrel-server
    if sys.platform.startswith('win32'):
        backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-server.exe")
    else:
        backend_launcher = "squirrel-server"
    print("[INFO] Launching Squirrel-server {}".format(backend_launcher))
    sys.stdout.flush()
    sys.stderr.flush()

    run([backend_launcher])

elif do_launch == "dev-server":
    # Launching Squirrel-devbackend, which doesn't serve the front end, and let the front
    # be served by 'gulp serve'
    if sys.platform.startswith('win32'):
        devbackend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-devbackend.exe")
    else:
        devbackend_launcher = "squirrel-devbackend"
    print("[INFO] Launching squirrel-devbackend {}".format(devbackend_launcher))
    sys.stdout.flush()
    sys.stderr.flush()

    run_background([devbackend_launcher])
    print("[INFO] Sleep 5 seconds")
    sys.stdout.flush()
    sys.stderr.flush()
    sleep(5)

    print("[INFO] Serving dev frontend")
    run(["gulp", "serve"], cwd=os.path.join(install_path, "frontend"), shell=shell)


print("[INFO] Done")
print("-------------------------------------------------------------------------------")
