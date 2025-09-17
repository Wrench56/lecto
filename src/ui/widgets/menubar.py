"""
Menu bar widget for the app window.
"""

from __future__ import annotations

import tkinter
from typing import Callable


class MenuBar:
    """
    Builds and attaches a top menubar to a Tk window.
    """
    def __init__(
        self,
        app: tkinter.Tk,
        *,
        on_open: Callable[[], None],
        on_quit: Callable[[], None],
        on_toggle_statusbar: Callable[[bool], None],
        on_about: Callable[[], None],
    ) -> None:
        self._app = app
        self._root = tkinter.Menu(app)
        self._statusbar_visible = tkinter.BooleanVar(value=True)

        file_menu = tkinter.Menu(self._root, tearoff=0)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=on_open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=on_quit)
        self._root.add_cascade(label="File", menu=file_menu)

        view_menu = tkinter.Menu(self._root, tearoff=0)
        view_menu.add_checkbutton(
            label="Status bar",
            onvalue=True,
            offvalue=False,
            variable=self._statusbar_visible,
            command=lambda: on_toggle_statusbar(bool(self._statusbar_visible.get())),
        )
        self._root.add_cascade(label="View", menu=view_menu)

        help_menu = tkinter.Menu(self._root, tearoff=0)
        help_menu.add_command(label="About lecto", command=on_about)
        self._root.add_cascade(label="Help", menu=help_menu)

    def pack(self) -> None:
        """Attach menubar to the window."""
        self._app.config(menu=self._root)
