#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import shutil

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "configs", "default.conf"))

with open(config_path) as f:
    config = f.readlines()

# todo: read this config file (we are in a virtualenv, can import yaml package)
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
workdir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "workdir"))
frontend_dist_path = os.path.abspath(os.path.join(root_path,
                                                  "frontend",
                                                  "dist"))
frontend_node_modules_path = os.path.abspath(os.path.join(root_path,
                                                          "frontend",
                                                          "node_modules"))
frontend_bower_components_path = os.path.abspath(os.path.join(root_path,
                                                              "frontend",
                                                              "bower_components"))

paths_to_remove = [(workdir_path, "workdir"),
                   (os.path.join(root_path, "_trial_temp"), "_trial_temp"),
                   (os.path.join(root_path, "_trial_temp.lock"), "_trial_temp.lock"),
                   (os.path.join(root_path, "tosource"), "tosource"),
                   (frontend_dist_path, "frontend/dist"),
                   (frontend_bower_components_path, "frontend/bower_components"),
                   ]

print("Uninstalling files in {}".format(root_path))
for path, name in paths_to_remove:
    if os.path.isdir(path):
        print("Removing {}...".format(name))
        shutil.rmtree(path)
    elif os.path.isfile(path):
        print("Removing {}...".format(name))
        os.unlink(path)

print("Uninstall done")
