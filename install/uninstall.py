#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Please remind that this script uses the system python install, so we are **not** in our well
# controlled virtual env.

import fnmatch
import imp
import os
import shutil
import sys


# Injecting available targets from installer stage 2
lib = imp.load_source('install-lib.py',
                      os.path.join(os.path.dirname(__file__), "install-lib.py"))

remove_dist = True

if len(sys.argv) > 1:
    args = sys.argv[:]
    if args[1] == "--no-dist":
        remove_dist = False

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))

with open(config_path) as f:
    config = f.readlines()

# todo: read this config file (beware, we are *not* in a virtualenv, cannot use the yaml package)
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
frontend_dist_path = os.path.abspath(os.path.join(root_path,
                                                  "frontend",
                                                  "dist"))
homepage_dist_path = os.path.abspath(os.path.join(root_path,
                                                  "homepage",
                                                  "dist"))
egg_info = os.path.abspath(os.path.join(root_path,
                                        "backend",
                                        "Squirrel.egg-info"))
frontend_node_modules_path = os.path.abspath(os.path.join(root_path,
                                                          "frontend",
                                                          "node_modules"))
frontend_bower_components_path = os.path.abspath(os.path.join(root_path,
                                                              "frontend",
                                                              "bower_components"))

frontend_po_path = os.path.abspath(os.path.join(root_path,
                                                "frontend",
                                                "src",
                                                "po",
                                                ))
homepage_node_modules_path = os.path.abspath(os.path.join(root_path,
                                                          "homepage",
                                                          "node_modules"))
homepage_bower_components_path = os.path.abspath(os.path.join(root_path,
                                                              "homepage",
                                                              "bower_components"))

homepage_po_path = os.path.abspath(os.path.join(root_path,
                                                "homepage",
                                                "src",
                                                "po",
                                                ))

paths_to_remove = [
    (os.path.join(root_path, "_trial_temp"), "_trial_temp"),
    (os.path.join(root_path, "_trial_temp.lock"), "_trial_temp.lock"),
    (frontend_node_modules_path, "frontend/node_modules"),
    (frontend_bower_components_path, "frontend/bower_components"),
    (homepage_node_modules_path, "homepage/node_modules"),
    (homepage_bower_components_path, "homepage/bower_components"),
]
if remove_dist:
    paths_to_remove.append((os.path.join(root_path, "tosource"), "tosource"))
    paths_to_remove.append((workdir_path, "workdir"))
    paths_to_remove.append((egg_info, "Squirrel.egg_info"))
    paths_to_remove.append((frontend_dist_path, "frontend/dist"))
    paths_to_remove.append((homepage_dist_path, "homepage/dist"))

lib.printInfo("Uninstalling files in {}".format(root_path))
for path, name in paths_to_remove:
    if os.path.isdir(path):
        lib.printInfo("Removing {}...".format(name))
        shutil.rmtree(path)
    elif os.path.isfile(path):
        lib.printInfo("Removing {}...".format(name))
        os.unlink(path)

file_pattern_to_clean = [
    '*.pyc',
    '*.pyo',
]
po_file_to_clean = [
    '*.js',
    '*.mo',
]
lib.printInfo("Cleaning files: {}".format(", ".join(file_pattern_to_clean)))
matches = []
for root, dirnames, filenames in os.walk(root_path):
    for pattern in file_pattern_to_clean:
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))

for root, dirnames, filenames in os.walk(frontend_po_path):
    for pattern in po_file_to_clean:
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
for root, dirnames, filenames in os.walk(homepage_po_path):
    for pattern in po_file_to_clean:
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
if matches:
    lib.printInfo("Removing:")
    for m in matches:
        lib.printInfo(" - {}".format(m))
        os.unlink(m)

if remove_dist:
    lib.printInfo("Uninstall done")
else:
    lib.printInfo("Uninstall of compilation artifacts done. Built dist kept.")
