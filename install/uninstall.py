#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Please remind that this script uses the system python install, so we are **not** in our well
# controlled virtual env.

import fnmatch
import os
import shutil

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))

with open(config_path) as f:
    config = f.readlines()

# todo: read this config file (beware, we are *not* in a virtualenv, cannot use the yaml package)
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
frontend_dist_path = os.path.abspath(os.path.join(root_path,
                                                  "frontend",
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

paths_to_remove = [
    (egg_info, "Squirrel.egg_info"),
    (os.path.join(root_path, "_trial_temp"), "_trial_temp"),
    (os.path.join(root_path, "_trial_temp.lock"), "_trial_temp.lock"),
    (os.path.join(root_path, "tosource"), "tosource"),
    (frontend_dist_path, "frontend/dist"),
    (frontend_node_modules_path, "frontend/node_modules"),
    (frontend_bower_components_path, "frontend/bower_components"),
    (workdir_path, "workdir"),
]

print("Uninstalling files in {}".format(root_path))
for path, name in paths_to_remove:
    if os.path.isdir(path):
        print("Removing {}...".format(name))
        shutil.rmtree(path)
    elif os.path.isfile(path):
        print("Removing {}...".format(name))
        os.unlink(path)

file_pattern_to_clean = [
    '*.pyc',
    '*.pyo',
]
po_file_to_clean = [
    '*.js',
    '*.mo',
]
print("Cleaning files: {}".format(", ".join(file_pattern_to_clean)))
matches = []
for root, dirnames, filenames in os.walk(root_path):
    for pattern in file_pattern_to_clean:
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))

for root, dirnames, filenames in os.walk(frontend_po_path):
    for pattern in po_file_to_clean:
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
if matches:
    print("Removing:")
    for m in matches:
        print(" - {}".format(m))
        os.unlink(m)

print("Uninstall done")
