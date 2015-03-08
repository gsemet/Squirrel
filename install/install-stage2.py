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

if not os.environ['VIRTUAL_ENV']:
    raise Exception("VIRTUAL_ENV environment variable is empty. We are not in a virtualenv.")

print("=======================================================================")
print("[INFO] Squirrel Installer Stage 2")
print("[INFO] We are in the virtualenv: {}".format(os.environ['VIRTUAL_ENV']))
print("[INFO] installation dir: {}".format(install_path))
print("[INFO] workdir: {}".format(workdir_path))
print("=======================================================================")


def run(cmd, cwd=None, shell=False):
    print("[CMD ] {}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)

print("[INFO] Installing backend requirements")
run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                          "requirements.txt")])

if sys.platform == 'win32':
    print("=======================================================================")
    print("[INFO] Installing Windows dependencies")
    run(["pip", "install", "-r", os.path.join(install_path, "backend",
                                              "requirements-win32.txt")])
    print("[INFO] Ensure you have win32api installed")


print("=======================================================================")
print("[INFO] Installing backend")
run(["pip", "install", "-e", os.path.join(install_path, "backend")])

if sys.platform == 'win32':
    shell = True
else:
    shell = False

print("=======================================================================")
print("[INFO] Compiling frontend website")
run(["npm", "install"], cwd=os.path.join(install_path, "frontend"), shell=shell)
run(["gulp", "build"], cwd=os.path.join(install_path, "frontend"), shell=shell)


print("=======================================================================")
print("[INFO] Building online documentation")
if sys.platform == 'win32':
    run(["make.bat", "html"], cwd=os.path.join(install_path, "doc"))
else:
    run(["make", "html"], cwd=os.path.join(install_path, "doc"), shell=shell)


print("=======================================================================")
# Launching Squirrel-backend
if sys.platform == 'win32':
    backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-backend.exe")
else:
    backend_launcher = "squirrel-backend"
print("[INFO] Launching Squirrel-backend {}".format(backend_launcher))
sys.stdout.flush()
sys.stderr.flush()

run([backend_launcher])

print("[INFO] Done")
print("=======================================================================")
