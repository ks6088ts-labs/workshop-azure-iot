import logging

from workshop_azure_iot.settings.core import CoreSettings


def get_logger(
    name: str,
) -> logging.Logger:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level=CoreSettings().core_log_level)

    return logger
