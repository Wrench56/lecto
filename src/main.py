"""
Entry file of lecto.
"""

import logging
import logger

from ui.app import App

def main() -> None:
    """Entry point of lecto."""
    l2e = logger.setup_logging()

    logging.info("Lecto started!")
    app = App(l2e)
    app.mainloop()

if __name__ == '__main__':
    main()
