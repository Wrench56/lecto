"""
Main app.
"""

import logging

import tkinter

from ui.widgets.statusbar import Statusbar

from logger import Log2EventFilter

class App(tkinter.Tk):
    """Main app class"""
    TITLE = 'lecto'

    def __init__(self, l2e: Log2EventFilter, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._l2e = l2e
        self._l2e.set_callback(self._callback)
        self._setup()

    def _setup(self) -> None:
        self.geometry('800x600')
        self.title(self.TITLE)

        self.statusbar = Statusbar(self)
        self.statusbar.pack()
        logging.info('App setup done!')

    def _callback(self, record: logging.LogRecord) -> None:
        self.statusbar.set_status(record)
