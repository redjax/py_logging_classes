import logging
from pathlib import Path


class LoggingFileHandlerBase(logging.FileHandler):
    """Base class for all Python logging FileHandler config classes."""

    def __init__(
        self,
        filename,
        level=logging.NOTSET,
        mode="a",
        encoding=None,
        delay=False,
        formatter=None,
        level_filter=None,
        propagate=True,
    ):
        logging_dir = Path(f"{filename}").parent
        try:
            logging_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError as perm_err:
            raise perm_err
        except Exception as exc:
            raise exc

        super().__init__(filename, mode, encoding, delay)
        self.setLevel(level=level)
        self.formatter = formatter
        self.level_filter = level_filter
        self.propagate = propagate

    def emit(self, record):
        if self.level_filter is not None:
            # Filter out messages below specified level
            if record.levelno >= self.level_filter:
                super().emit(record)
        else:
            super().emit(record)


class LoggingFileHandler(LoggingFileHandlerBase):
    pass
