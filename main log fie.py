import logging

# Set up logging
logging.basicConfig(filename='F:/python project/file transfer/server-file.txt', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
