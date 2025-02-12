import os
import logging
import sys 

log_dir = 'logs'
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(
    level=logging.INFO,
    format=format,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")
