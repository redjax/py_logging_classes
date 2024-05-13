import sys
from pathlib import Path
import logging


class CustomLogger:
    def __init__(self, name, level=logging.NOTSET, handlers=None):
        self.name = name
        self.level = level
        self.handlers = handlers or []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)

        for handler in self.handlers:
            handler.setLevel(self.level)
            handler.setFormatter(handler.formatter.get_formatter())
            logger.addHandler(handler)

        return logger
