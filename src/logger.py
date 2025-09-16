import logging
import sys
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter


class Log2EventFilter(logging.Filter):
    def __init__(self) -> None:
        super().__init__(name='Log2EventFilter')
        self._callback = None

    def filter(self, record) -> bool:
        """Hijack logging and pass record to callback"""
        if self._callback is not None:
            self._callback(record)
        return True

    def set_callback(self, callback: callable) -> None:
        self._callback = callback


def setup_logging():
    """Set up custom logger."""
    print(' Date               | Module               | [LEVL]    Message')
    print('                    |                      | [    ]')
    formatter = ColoredFormatter(
       '%(asctime)s | %(module)-20s | [%(log_color)s%(levelname)s%(reset)s]    %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        reset=True,
        log_colors={
            'DBUG': 'cyan',
            'INFO': 'green',
            'WARN': 'yellow',
            'ERRO': 'red',
            'CRIT': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    custom_formatter = logging.Formatter(
        fmt="%(asctime)s | %(module)-20s | [%(levelname)s]   %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    priority_terminal = logging.StreamHandler(sys.stdout)
    priority_terminal.setLevel(logging.DEBUG)
    priority_terminal.setFormatter(formatter)

    log_file_handler = RotatingFileHandler(
        filename="./logs/logfile.log",
        maxBytes=16 * 1024 * 1024,
        backupCount=20,
        encoding="utf-8"
    )
    log_file_handler.setLevel(logging.DEBUG)
    log_file_handler.setFormatter(custom_formatter)

    logging.addLevelName(logging.DEBUG, 'DBUG')
    logging.addLevelName(logging.INFO, 'INFO')
    logging.addLevelName(logging.WARNING, 'WARN')
    logging.addLevelName(logging.ERROR, 'ERRO')
    logging.addLevelName(logging.CRITICAL, 'CRIT')

    logging.basicConfig(level=logging.DEBUG, handlers=(priority_terminal, log_file_handler,))

    log2event_filter = Log2EventFilter()
    logging.getLogger().addFilter(log2event_filter)

    logging.debug("Logging has been configured!")
    return log2event_filter
