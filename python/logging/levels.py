# coding=utf-8
'''
Level       value
CRITICAL    50
ERROR       40
WARNING     30
INFO        20
DEBUG       10
NOTSET       0
'''

import logging
import sys

levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'critical': logging.CRITICAL,
    'warning': logging.WARNING,
    'error': logging.ERROR,
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = levels.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')