from _logging._defaults import DEFAULT_DATE_FORMAT, DEFAULT_LOGMSG_FORMAT
import logging


class LoggingFormatter:
    def __init__(
        self,
        fmt: str = DEFAULT_LOGMSG_FORMAT,
        datefmt: str = DEFAULT_DATE_FORMAT,
        style: str = "%",
    ):
        self.fmt = fmt
        self.datefmt = datefmt
        self.style = style

    def get_formatter(self):
        return logging.Formatter(fmt=self.fmt, datefmt=self.datefmt, style=self.style)
