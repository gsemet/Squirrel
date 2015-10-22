# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import logging.config as logging_config
import psutil
import re
import signal
import subprocess
import sys
import time

from argh import arg
from argh import dispatch_command
from argh import expects_obj
from watchdog.observers import Observer
from watchdog.tricks import AutoRestartTrick
from watchdog.utils import echo

VERSION_STRING = "0.0.1"

log = logging.getLogger(__name__)

# Extracted from watchmedo demo script from watchdog
#


class SquirrelAutoRestartTrick(AutoRestartTrick):

    """Starts a long-running subprocess and restarts it on matched events.

    The command parameter is a list of command arguments, such as
    ['bin/myserver', '-c', 'etc/myconfig.ini'].

    Call start() after creating the Trick. Call stop() when stopping
    the process.
    """

    def __init__(self,
                 command,
                 patterns=None,
                 ignore_patterns=None,
                 ignore_directories=False,
                 stop_signal=signal.SIGINT,
                 kill_after=10,
                 sleep_between_restart=1,
                 shell=False,
                 win32_safe_kill=False,
                 ):
        super(SquirrelAutoRestartTrick, self).__init__(
            command=command, patterns=patterns, ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories, stop_signal=stop_signal,
            kill_after=kill_after)
        self.command = command
        self.shell = shell
        self.sleep_between_restart = sleep_between_restart
        self.win32_safe_kill = win32_safe_kill

    def start(self):
        self.process = subprocess.Popen(self.command, shell=self.shell)
        logging.debug("Started with pid {}".format(self.process.pid))

    def stop(self):
        if self.process is None:
            return
        try:
            if sys.platform.startswith("win32") and self.win32_safe_kill:
                logging.debug("Win32 safe killing: using taskkill /T /F on pid {}".format(self.process.pid))
                subprocess.check_call("taskkill /PID {} /T /F".format(self.process.pid))
            else:
                logging.debug("Killing subprocess {}".format(self.process.pid))
                proc = psutil.Process(self.process.pid)
                proc.kill()
        except subprocess.CalledProcessError:
            # already dead
            pass
        except psutil.NoSuchProcess:
            logging.debug("Warning: no such process. Continuing")
            # if process already dead, just let the AutoRestartTrick restarts it
            pass
        else:
            kill_time = time.time() + self.kill_after
            logging.debug("Testing if pid {} is still alive".format(self.process.pid))
            while time.time() < kill_time:
                if self.process.poll() is not None:
                    break
                time.sleep(0.25)
            else:
                logging.debug("Process still alive, terminating pid {}".format(self.process.pid))
                try:
                    proc = psutil.Process(self.process.pid)
                    proc.terminate()
                except psutil.NoSuchProcess:
                    logging.debug("Warning: no such process. Continuing")
                    # if process already dead, just let the AutoRestartTrick restarts it
                    pass
        self.process = None

    @echo.echo
    def on_any_event(self, event):
        logging.debug("Stopping subprocess")
        self.stop()
        if self.sleep_between_restart:
            logging.debug("Subprocess killed, waiting {} seconds".format(self.sleep_between_restart))
            time.sleep(self.sleep_between_restart)
            logging.debug("Starting subprocess")
        else:
            logging.debug("Subprocess killed - Starting new subprocess")
        self.start()


def parse_patterns(patterns_spec, ignore_patterns_spec, separator=';'):
    """
    Parses pattern argument specs and returns a two-tuple of
    (patterns, ignore_patterns).
    """
    patterns = patterns_spec.split(separator)
    ignore_patterns = ignore_patterns_spec.split(separator)
    if ignore_patterns == ['']:
        ignore_patterns = []
    return (patterns, ignore_patterns)


def observe_with(observer, event_handler, pathnames, recursive):
    """
    Single observer thread with a scheduled path and event handler.

    :param observer:
        The observer thread.
    :param event_handler:
        Event handler which will be called in response to file system events.
    :param pathnames:
        A list of pathnames to monitor.
    :param recursive:
        ``True`` if recursive; ``False`` otherwise.
    """
    for pathname in set(pathnames):
        observer.schedule(event_handler, pathname, recursive)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


@arg('command',
     help='''Long-running command to run in a subprocess.
''')
@arg('command_args',
     metavar='arg',
     nargs='*',
     help='''Command arguments.

Note: Use -- before the command arguments, otherwise watchmedo will
try to interpret them.
''')
@arg('-d',
     '--directory',
     dest='directories',
     metavar='directory',
     action='append',
     help='Directory to watch. Use another -d or --directory option '
          'for each directory.')
@arg('-p',
     '--pattern',
     '--patterns',
     dest='patterns',
     default='*',
     help='matches event paths with these patterns (separated by ;).')
@arg('-i',
     '--ignore-pattern',
     '--ignore-patterns',
     dest='ignore_patterns',
     default='',
     help='ignores event paths with these patterns (separated by ;).')
@arg('-D',
     '--ignore-directories',
     dest='ignore_directories',
     default=False,
     help='ignores events for directories')
@arg('-R',
     '--recursive',
     dest='recursive',
     default=False,
     help='monitors the directories recursively')
@arg('--interval',
     '--timeout',
     dest='timeout',
     default=1.0,
     help='use this as the polling interval/blocking timeout')
@arg('--signal',
     dest='signal',
     default='SIGINT',
     help='stop the subprocess with this signal (default SIGINT)')
@arg('--kill-after',
     dest='kill_after',
     default=10.0,
     help=('when stopping, kill the subprocess after the specified timeout '
           '(default 10)'))
@arg('--sleep-between-restart',
     dest="sleep_between_restart",
     default=5,
     help='Time to wait between two restart (default 1 second)')
@arg('--shell',
     action='store_true',
     dest="shell",
     help="Launch sub command in a shell (cmd under windows)")
@arg('--verbose', "-v",
     action='store_true',
     dest="verbose",
     help="Print debug information")
@arg('--win32-safe-kill',
     action='store_true',
     dest="win32_safe_kill",
     help="On Windows, use taskkill /T to kill (needed for twisted application)")
@arg('--version',
     action='version',
     version='%(prog)s ' + VERSION_STRING)
@expects_obj
def auto_restart(args):
    """
    Subcommand to start a long-running subprocess and restart it
    on matched events.
    :param args:
        Command line argument options.
    """
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    logging.info("Auto relauncher with the following command: {}".format(args.command))
    logging.debug("  directory: {}".format(args.directories))
    logging.debug("  shell: {}".format(args.shell))
    if sys.platform.startswith("win32"):
        logging.debug("  win32 safe kill: {}".format(args.win32_safe_kill))
    logging.debug("  Wait time between restart: {} second(s)".format(args.sleep_between_restart))
    if not args.directories:
        args.directories = None

    # Allow either signal name or number.
    if re.match('^SIG[A-Z]+$', args.signal):
        stop_signal = getattr(signal, args.signal)
    else:
        stop_signal = int(args.signal)

    # Handle SIGTERM in the same manner as SIGINT so that
    # this program has a chance to stop the child process.
    def handle_sigterm(_signum, _frame):
        raise KeyboardInterrupt()

    signal.signal(signal.SIGTERM, handle_sigterm)

    patterns, ignore_patterns = parse_patterns(args.patterns,
                                               args.ignore_patterns)
    command = [args.command]
    command.extend(args.command_args)
    handler = SquirrelAutoRestartTrick(command=command,
                                       patterns=patterns,
                                       ignore_patterns=ignore_patterns,
                                       ignore_directories=args.ignore_directories,
                                       stop_signal=stop_signal,
                                       kill_after=args.kill_after,
                                       sleep_between_restart=args.sleep_between_restart,
                                       shell=args.shell,
                                       win32_safe_kill=args.win32_safe_kill,
                                       )
    handler.start()
    observer = Observer(timeout=args.timeout)
    observe_with(observer, handler, args.directories, args.recursive)
    handler.stop()


def run():

    def terminate_handler(signum, frame):
        print('Signal handler called with signal', signum)
        sys.exit(0)

    def kill_handler(signum, frame):
        print('Signal handler called with signal', signum)
        sys.exit(1)

    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGTERM, terminate_handler)
    signal.signal(signal.SIGINT, kill_handler)
    if hasattr(signal, "SIGBREAK"):
        signal.signal(signal.SIGBREAK, terminate_handler)

    logging_config.dictConfig({
        'version': 1,
        'formatters': {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': "%(log_color)s{%(levelname)5s}%(reset)s %(message)s",
                'log_colors': {
                    'DEBUG':    'cyan',
                    'INFO':     'green',
                    'WARNING':  'yellow',
                    'ERROR':    'red',
                    'CRITICAL': 'red,bg_white',
                },
            }
        },
        'handlers': {
            'stream': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'level': 'DEBUG'
            },
        },
        'loggers': {
            '': {
                'handlers': ['stream'],
                'level': 'DEBUG',
            },
        },
    })
    dispatch_command(auto_restart)
