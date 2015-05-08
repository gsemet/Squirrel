from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    # python < 3
    import ConfigParser as configparser
except:
    # python > 3
    import configparser

import logging
import logging.config as logging_config
import sys

from StringIO import StringIO
from colorlog import ColoredFormatter
from copy import deepcopy
from functools import partial
from subprocess import PIPE
from subprocess import check_output

from squirrel.services.config import Config


log = logging.getLogger(__name__)


def setupLogger():
    config_file_fullpath = Config().logging.config_file_fullpath
    log.info("Using configuration file: {}".format(config_file_fullpath))
    try:
        logging_config.fileConfig(config_file_fullpath)
    except configparser.NoSectionError as e:
        raise type(e)("NoSectionError exception raised by fileConfig. "
                      "This probably comes from an invalid path: {!r}\n"
                      "Original exception message: {}".format(config_file_fullpath, e))

    align_level_width = 6
    extra_char_width = 3

    class SplitFormatter(ColoredFormatter):

        '''
        Magic Formatter that gracefully handles multiline logs, ie it split the multiline strings
        and add each log independently.

        This handles two spliting:

        - if the terminal width is found, try to fit the output in the terminal by splitting the
          string arbitrarily
        - if the record message is multiline, split it and print prefix (loglevel, date,...)
          independently

        Note this only impacts the display to stdout handler, not the record storage, so
        if these logs are sent to another handler (for instance to splunk handler), the log
        will not be split
        '''

        def __init__(self, termWidth=-1, *args, **kwargs):
            super(SplitFormatter, self).__init__(*args, **kwargs)
            # Try to retrieve the terminal width:
            if termWidth == -1:
                if sys.platform.startswith("win32"):
                    w = self.getWin32TerminalSize()
                    if w:
                        termWidth = w[0] - align_level_width - extra_char_width - 1
                else:
                    try:
                        # redirecting the stderr to an unused PIPE, to avoid the following issue:
                        #     'stty: standard input: Invalid argument'
                        # when executed from a step ShellCommand
                        data = check_output(['stty', 'size'], stderr=PIPE)
                        _, columns = data.split()
                        if columns > 0:
                            termWidth = columns
                    except:
                        pass
                    termWidth = int(termWidth) - align_level_width - extra_char_width
            self.termWidth = termWidth

        def format(self, record):
            record = deepcopy(record)
            multiline_message = record.getMessage()
            if self.usesTime():
                record.asctime = self.formatTime(record, self.datefmt)
            formatted_lines = []
            for line in multiline_message.split("\n"):
                sublines = [l for l in iter(partial(StringIO(line).read, int(self.termWidth)), '')]
                if not sublines:
                    # If the string is empty but we have a record, still add an empty record in the
                    # output.
                    record.msg = ""
                    s = super(SplitFormatter, self).format(record)
                    formatted_lines.append(s)
                else:
                    for subline in sublines:
                        record.msg = subline
                        s = super(SplitFormatter, self).format(record)
                        formatted_lines.append(s)
            return "\n".join(formatted_lines)

        # http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
        def getWin32TerminalSize(self):
            res = None
            try:
                from ctypes import windll, create_string_buffer

                # stdin handle is -10
                # stdout handle is -11
                # stderr handle is -12

                h = windll.kernel32.GetStdHandle(-12)
                csbi = create_string_buffer(22)
                res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
            except:
                return None
            if res:
                import struct
                (bufx, bufy, curx, cury, wattr,
                 left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                sizex = right - left + 1
                sizey = bottom - top + 1
                return sizex, sizey
            else:
                return None

    if Config().logging.use_split_formatter:
        log.debug("Configuring magic split formatter")

        format_string = ("%(log_color)s%(levelname){align_level_width}s%(reset)s | %(message)s"
                         .format(align_level_width=align_level_width))
        root = logging.getLogger()
        date_fmt_string = None
        # Do *not* replace the formatter in quiet mode since we want to bare output
        root.handlers[0].setFormatter(SplitFormatter(fmt=format_string,
                                                     datefmt=date_fmt_string,
                                                     reset=True,
                                                     log_colors={
                                                         'DEBUG':    'cyan',
                                                         'INFO':     'green',
                                                         'WARNING':  'yellow',
                                                         'ERROR':    'red',
                                                         'CRITICAL': 'red,bg_white',
                                                     },
                                                     secondary_log_colors={},
                                                     style='%'
                                                     ))
    elif Config().logging.use_color_formatter:
        log.debug("Configuring color formatter")

        format_string = ("%(log_color)s%(levelname){align_level_width}s%(reset)s | %(message)s"
                         .format(align_level_width=align_level_width))
        root = logging.getLogger()
        date_fmt_string = None
        # Do *not* replace the formatter in quiet mode since we want to bare output
        root.handlers[0].setFormatter(ColoredFormatter(fmt=format_string,
                                                       datefmt=date_fmt_string,
                                                       reset=True,
                                                       log_colors={
                                                           'DEBUG':    'cyan',
                                                           'INFO':     'green',
                                                           'WARNING':  'yellow',
                                                           'ERROR':    'red',
                                                           'CRITICAL': 'red,bg_white',
                                                       },
                                                       secondary_log_colors={},
                                                       style='%'
                                                       ))
    log.info("*" * 79)
    log.info("*" + " " * 26 + "Starting Squirrel Server " + " " * 26 + "*")
    log.info("*" * 79)
    log.info("Logging configured - Entering in a colorful world on your terminal!")

    log.debug("File loggers configured by: {}".format(config_file_fullpath))
