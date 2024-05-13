import logging
from logging_classes._logging import (
    DEFAULT_DATE_FORMAT,
    DEFAULT_LOGMSG_FORMAT,
    LoggingFormatter,
    LoggingStdoutHandler,
    LoggingStderrHandler,
    LoggingFileHandler,
    CustomLogger,
)

formatter = LoggingFormatter()

stdout_handler = LoggingStdoutHandler(formatter=formatter)
stderr_handler = LoggingStderrHandler(formatter=formatter)
file_handler = LoggingFileHandler(
    filename="logs/app.log", level=logging.DEBUG, formatter=formatter
)
err_file_handler = LoggingFileHandler(
    filename="logs/err.log",
    level=logging.ERROR,
    formatter=formatter,
    level_filter=logging.ERROR,
)

# Create CustomLogger instance
custom_logger = CustomLogger(
    name=__name__,
    level=logging.DEBUG,
    handlers=[stdout_handler, file_handler, err_file_handler],
)

log = custom_logger.get_logger()

log.info("Test INFO")
log.debug("Test DEBUG")
log.warning("Test WARNING")
log.error("Test ERROR")
log.critical("Test CRITICAL")


"""
## Create formatter
formatter = LoggingFormatter()

## Create handlers
console_handler = LoggingHandler(level=logging.DEBUG, formatter=formatter)
file_handler = LoggingHandler(level=logging.INFO)

## Create custom logger
logger = CustomLogger(name=__name__, level=logging.INFO)
logger.add_handler(console_handler)
logger.add_handler(file_handler)
logger.set_formatter(formatter)

## Configure logging
logger.configure_logging()

## Get logger instance
log = logger.get_logger()

if __name__ == "__main__":
    log.info("Test INFO message")
    log.debug(f"Test DEBUG message")
    log.warning(f"Test WARNING message")
    log.error(f"Test ERROR message")
    log.critical(f"Test CRITICAL message")
"""
