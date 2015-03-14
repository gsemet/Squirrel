# This is the second part of the installation procedure or Squirrel.
# It should be executed from the virtualenv

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess
import sys

install_path = sys.argv[1]
install_path = os.path.abspath(install_path)

workdir_path = sys.argv[2]
workdir_path = os.path.abspath(workdir_path)

launch = sys.argv[3]

if not os.environ['VIRTUAL_ENV']:
    raise Exception("VIRTUAL_ENV environment variable is empty. We are not in a virtualenv.")

print("===============================================================================")
print("[INFO] Squirrel Installer Stage 2")
print("[INFO] We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
print("[INFO] installation dir: {}".format(install_path))
print("[INFO] workdir: {}".format(workdir_path))
print("[INFO] Launch: {}".format(launch))
print("===============================================================================")
print("")


def run(cmd, cwd=None, shell=False):
    print("[CMD ] {}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def call(cmd, cwd=None, shell=False):
    print("[CMD ] {}".format(" ".join(cmd)))
    return subprocess.call(cmd, shell=shell, cwd=cwd)


if sys.platform.startswith("linux"):
    print("===============================================================================")
    pip_version_str = subprocess.check_output(["pip", "--versio"])
    pip_version_str = pip_version_str.split(" ")[1]
    pip_version_str = pip_version_str.split("-")[0]
    pip_version_str = pip_version_str.split("_")[0]
    pip_version_str = pip_version_str.rpartition(".")[0]
    pip_major, _, pip_minor = pip_version_str.partition(".")
    pip_version = int(pip_major) * 100 + int(pip_minor)
    if pip_version <= 105:
        print("[INFO] Patching this pip (version) {}.{}), to fix proxy issue (fixed in pip 1.6)".format(pip_major,
                                                                                                        pip_minor))
        print("[INFO] See: https://github.com/pypa/pip/issues/1805")
        # Patching the installed pip to fix the following bug with proxy
        # See http://www.irvingc.com/posts/10
        patch_path = os.path.join(install_path, "install", "patch-pip.patch")
        c = call(["bash", "-c", "patch -p0 -N --dry-run --silent < {} 2>/dev/null".format(patch_path)])
        if not c:
            print("[INFO] Applying patch")
            run(["bash", "-c", "patch -p0 < {}".format(patch_path)])
        else:
            print("[INFO] Already applied. Skipping patch")

print("===============================================================================")
print("[INFO] Installing backend requirements")
run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                          "requirements.txt")])

if sys.platform.startswith('win32'):
    print("===============================================================================")
    print("[INFO] Installing Windows dependencies")
    run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                              "requirements-win32.txt")])
    print("[INFO] Ensure you have win32api installed")


print("===============================================================================")
print("[INFO] Installing backend")
run(["pip", "install", "-e", os.path.join(install_path, "backend")])

if sys.platform.startswith('win32'):
    shell = True
else:
    shell = False

print("===============================================================================")
print("[INFO] Compiling frontend website")
if "http_proxy" in os.environ:
    print("[INFO] Behind a proxy: npm --proxy")
    run(["npm", "config", "set", "strict-ssl", "false"], cwd=os.path.join(install_path,
                                                                          "frontend"),
        shell=shell)
    run(["npm", "--proxy", os.environ["http_proxy"], "install"], cwd=os.path.join(install_path,
                                                                                  "frontend"),
        shell=shell)
else:
    run(["npm", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)
run(["bower", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)
run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"), shell=shell)


print("===============================================================================")
print("[INFO] Building online documentation")
if sys.platform.startswith('win32'):
    run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"), shell=True)
else:
    run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)

if launch != "launch":
    print("")
    print("===============================================================================")
    print("Do not start the server. Install is succesful.")
    print("===============================================================================")
    sys.exit(0)

print("===============================================================================")
# Launching Squirrel-backend
if sys.platform.startswith('win32'):
    backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-backend.exe")
else:
    backend_launcher = "squirrel-backend"
print("[INFO] Launching Squirrel-backend {}".format(backend_launcher))
sys.stdout.flush()
sys.stderr.flush()

run([backend_launcher])

print("[INFO] Done")
print("===============================================================================")
