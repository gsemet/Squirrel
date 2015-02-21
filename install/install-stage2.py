import os
import sys
import subprocess

print sys.argv

install_path = sys.argv[1]
install_path = os.path.abspath(install_path)

workdir_path = sys.argv[2]
workdir_path = os.path.abspath(workdir_path)


print "Squirrel Installer Stage 2"
print "Should be in the virtualenv"
print "installation dir: {}".format(install_path)
print "workdir: {}".format(workdir_path)

print "Installing dependencies..."
subprocess.check_call(["pip", "install", "-r", os.path.join(install_path, "backend", "requirements.txt")])

print "Installing backend"
subprocess.check_call(["pip", "install", "-e", os.path.join(install_path, "backend")])

backend_launcher = os.path.join(workdir_path, "Scripts", "squirrel-backend.exe")
print "Launching Squirrel-backend {}".format(backend_launcher)
sys.stdout.flush()
sys.stderr.flush()

subprocess.check_call([backend_launcher])

print "Done"
