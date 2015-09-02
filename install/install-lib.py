from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess
import sys

isWindows = False
if sys.platform.startswith('win32'):
    isWindows = True

####################################################################################################
# Utility functions
####################################################################################################


class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOOT = '\033[94m'

    ENDC = '\033[0m'

# Do *not* use color when:
#  - on windows
#  - not in a terminal except if we are in Travis CI
if isWindows or (not os.environ.get("TRAVIS") and not sys.stdout.isatty()):
    bcolors.HEADER = ''
    bcolors.OKBLUE = ''
    bcolors.OKGREEN = ''
    bcolors.WARNING = ''
    bcolors.FAIL = ''
    bcolors.BOLD = ''
    bcolors.UNDERLINE = ''
    bcolors.BOOT = ''
    bcolors.ENDC = ''


def flush():
    sys.stdout.flush()
    sys.stderr.flush()


def printInfo(text):
    print(bcolors.OKBLUE + "[INFO ] " + bcolors.ENDC + text)
    flush()


def printError(text):
    print(bcolors.FAIL + "[ERROR] " + bcolors.ENDC + text, file=sys.stderr)
    flush()


def printSeparator(char="-", color=bcolors.OKGREEN):
    print(color + char * 79 + bcolors.ENDC)
    flush()


def printNote(text):
    print(bcolors.HEADER + "[NOTE ] " + bcolors.ENDC + text)
    flush()


def printBoot(text):
    print(bcolors.BOOT + "[BOOT ] " + bcolors.ENDC + text)
    flush()


def run(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def run_output(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    s = subprocess.check_call(cmd, shell=shell, cwd=cwd)
    return str(s)


def run_nocheck(cmd, cwd=None, shell=False):
    try:
        print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
        flush()
        subprocess.check_call(cmd, shell=shell, cwd=cwd)
    except Exception as e:
        printError("Exception : {}".format(e))


def call(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def run_background(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD (background)" + bcolors.ENDC + "] {}".format(" ".join(cmd)))
    flush()
    subprocess.Popen(cmd, cwd=cwd, shell=shell)

####################################################################################################
