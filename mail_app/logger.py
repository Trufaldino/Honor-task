import logging
import os
from dotenv import load_dotenv
import sys
from logging.handlers import RotatingFileHandler


load_dotenv()

# Get the directory for storing logs from environment variables
LOGS_DIR = os.getenv("LOGS_DIR")

# Create the logs directory if it doesn't exist
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Create a logger instance
logger = logging.getLogger(__name__)

# Define log message format
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Create a rotating file handler to manage log files
file_handler = RotatingFileHandler(
    os.path.join(LOGS_DIR, "logfile.txt"), maxBytes=1000000, backupCount=5
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Set the log level to INFO
logger.setLevel(logging.INFO)

# Create a stream handler for logging to the console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
