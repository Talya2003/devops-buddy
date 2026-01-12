import logging
from app.core.config import settings


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("devops-buddy")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()

    if settings.APP_ENV == "development":
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s - %(message)s"
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger


logger = setup_logger()
