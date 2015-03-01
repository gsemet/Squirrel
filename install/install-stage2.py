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


print("Squirrel Installer Stage 2")
print("Should be in the virtualenv")
print("installation dir: {}".format(install_path))
print("workdir: {}".format(workdir_path))

print("Installing dependencies...")
subprocess.check_call(["pip", "install", "-r", os.path.join(install_path, "backend",
                                                            "requirements.txt")])

if sys.platform == 'win32':
    print("Installing Windows dependencies")
    subprocess.check_call(["pip", "install", "-r", os.path.join(install_path, "backend",
                                                                "requirements-win32.txt")])
    print("Ensure you have win32api installed")

print("Installing backend")
subprocess.check_call(["pip", "install", "-e", os.path.join(install_path, "backend")])

print("Compiling frontend website")
subprocess.check_call(["gulp", "build"], shell=True, cwd=os.path.join(install_path, "frontend"))

print("Building online documentation")
subprocess.check_call(["make.bat", "html"], shell=True, cwd=os.path.join(install_path, "doc"))

if sys.platform == 'win32':
    backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-backend.exe")
else:
    backend_launcher = "squirrel-backend"
print("Launching Squirrel-backend {}".format(backend_launcher))
sys.stdout.flush()
sys.stderr.flush()

subprocess.check_call([backend_launcher])

print("Done")
