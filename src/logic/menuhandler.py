"""
Handler for menu items
"""

from ui.widgets.statusbar import Statusbar

import logging

import sys

import webbrowser
import tkinter
import tkinter.filedialog

def exit() -> None:
    """Gracefully exit the program"""
    logging.info('Shutting down...')
    sys.exit(0)

def about() -> None:
    """Show project on GitHub"""
    webbrowser.open_new('https://github.com/Wrench56/lecto')

def toggle_statusbar(visible: bool, statusbar: Statusbar) -> None:
    """Toggle statusbar visibility"""
    statusbar.set_visible(visible)

def open() -> None:
    """Open a pdf."""
    filepath = tkinter.filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",
        filetypes=(("PDF files", "*.pdf",), ("All files", "*.*",),)
    )

    if not filepath:
        return
    logging.info('File opened: %s', filepath)
