"""
Statusbar widget.
"""

from typing import override

import logging

import tkinter

class Statusbar(tkinter.Frame):
    """Bottom statusbar widget"""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(bg='lightgrey', *args, **kwargs)
        self._setup_widgets()

    def _setup_widgets(self) -> None:
        self._s_msg = tkinter.Text(self, width=50, height=1, borderwidth=0, highlightthickness=0, relief='flat', bg='lightgrey')
        self._s_msg.insert(tkinter.END, 'Loading...')
        self._s_msg.tag_configure('dbug', foreground='blue')
        self._s_msg.tag_configure('info', foreground='green')
        self._s_msg.tag_configure('warn', foreground='yellow')
        self._s_msg.tag_configure('erro', foreground='red')
        self._s_msg.tag_configure('crit', foreground='red')
        self._s_msg.config(state='disabled')
        self._s_msg.pack(side=tkinter.LEFT)

    @override
    def pack(self) -> None:
        """Pack a widget in the parent widget."""
        super().pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def set_status(self, record: logging.LogRecord) -> None:
        """Set the status text"""
        message = record.getMessage().strip()
        self._s_msg.config(state='normal')
        self._s_msg.delete(1.0, tkinter.END)
        self._s_msg.insert(tkinter.END, f'[{record.levelname}] {message}')
        self._s_msg.tag_add(record.levelname.lower(), 1.1, 1.5)
        self._s_msg.config(state='disabled')
