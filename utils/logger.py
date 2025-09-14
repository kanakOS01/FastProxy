import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(name: str = "FastProxy") -> logging.Logger:
    """Configure and return a logger"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers: # avoid duplicate handlers
        return logger
    
    # --- Formatter ---
    formatter = logging.Formatter(
        fmt="[%(asctime)s] - [%(levelname)-s] | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # --- Console Handler ---
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # --- File Handler (rotating) ---
    file_handler = RotatingFileHandler(
        log_dir / "fastproxy.log", maxBytes=5_000_000, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
