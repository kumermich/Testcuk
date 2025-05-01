import logging
import sys

# Create logger
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger logger.addHandler(file_handler)
logger.addHandler(console_handler)
# Log some messages 
logger.debug('Debug message') 
logger.info('Info message')
logger.warning('Warning message')
