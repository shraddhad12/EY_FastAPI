import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='addition.log',
                    filemode='w')

# Create a logger object
logger = logging.getLogger(__name__)