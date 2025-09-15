import logging
import sys
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter



def setup_logging():
    print(' Date               | Module               | [LEVEL]    Message')
    print('                    |                      | [     ]')
    formatter = ColoredFormatter(
       '%(asctime)s | %(module)-20s | [%(log_color)s%(levelname)s%(reset)s]    %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO ': 'green',
            'WARN ': 'yellow',
            'ERROR': 'red',
            'CRIT ': 'red,bg_white',
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

    logging.addLevelName(logging.INFO, 'INFO ')
    logging.addLevelName(logging.WARNING, 'WARN ')
    logging.addLevelName(logging.CRITICAL, 'CRIT ')

    logging.basicConfig(level=logging.DEBUG, handlers=(priority_terminal, log_file_handler,))

    logging.debug("Logging has been configured!")
