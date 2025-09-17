"""
Main app.
"""

import logging

import tkinter

from ui.widgets.statusbar import Statusbar
from ui.widgets.menubar import MenuBar

from logic import menuhandler

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

        self._statusbar = Statusbar(self)
        self._statusbar.pack()

        self._menubar = MenuBar(self,
                               on_open=menuhandler.open,
                               on_about=menuhandler.about,
                               on_quit=menuhandler.exit,
                               on_toggle_statusbar=lambda visible: menuhandler.toggle_statusbar(visible, self._statusbar)
                              )
        self._menubar.pack()

        logging.info('App setup done!')

    def _callback(self, record: logging.LogRecord) -> None:
        self._statusbar.set_status(record)
