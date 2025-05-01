import logging

# Configure logging to write to a file
logging.basicConfig( level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='app.log',
       filemode='w'
)

logger = logging.getLogger( name ) logger.info('Starting the application')
logger.warning('This is a warning message')
