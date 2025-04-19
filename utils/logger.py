import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("phishing_logger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if already set
    if not logger.handlers:
        handler = RotatingFileHandler("logs/app.log", maxBytes=500_000, backupCount=3)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
