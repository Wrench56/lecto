import logging
import logger


def main() -> None:
    logger.setup_logging()

    logging.info("Lecto started!")

if __name__ == '__main__':
    main()
