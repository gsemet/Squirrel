#!/usr/bin/env python

import os
import shutil

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))

with open(config_path) as f:
    config = f.readlines()

workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))

if os.path.isdir(workdir_path):
    print "Removing workdir..."
    shutil.rmtree(workdir_path)
if os.path.isdir("_trial_temp"):
    print "Removing _trial_temp..."
    shutil.rmtree("_trial_temp")
if os.path.isdir("_trial_temp.lock"):
    print "Removing _trial_temp.lock..."
    shutil.rmtree("_trial_temp.lock")
if os.path.isfile("tosource"):
    print "Removing tosource..."
    os.unlink("tosource")

print "Uninstall done"
