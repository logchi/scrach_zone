import os
import glob
import logging
from logging.handlers import RotatingFileHandler

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d %(levelname)s - %(message)s}")
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=10, backupCount=2)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
my_logger.addHandler(handler)

for i in range(20):
    my_logger.debug('i = %d' % i)

logfiles = glob.glob('%s*' % LOG_FILENAME)
for f in logfiles:
    print(f)

# for f in logfiles:
#     os.remove(f)
