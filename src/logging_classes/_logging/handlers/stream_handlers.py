import logging
import sys


class LoggingStreamHandlerBase(logging.StreamHandler):
    """Base class for all Python logging StreamHandler config classes."""

    def __init__(self, formatter=None, stream=None, propagate=True):
        if stream is None:
            stream = sys.stdout if self.stream_is_stdout() else sys.stderr
        super().__init__(stream)
        self.formatter = formatter
        self.propagate = propagate

    def stream_is_stdout(self):
        raise NotImplementedError(
            "Method stream_is_stdout() must be implemented by subclass"
        )


class LoggingStdoutHandler(LoggingStreamHandlerBase):
    def stream_is_stdout(self):
        return True


class LoggingStderrHandler(LoggingStreamHandlerBase):
    def stream_is_stdout(self):
        return False
