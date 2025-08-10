import logging
import sys

def setup_logging():
    logger = logging.getLogger("backend_logger")
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler(stream=sys.stdout)
    file_handler = logging.FileHandler("backend.log", "a")

    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    console_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)


    logger.addHandler(console_handler)
    logger.addHandler(file_handler)