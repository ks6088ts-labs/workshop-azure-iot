import logging

logger = logging.getLogger(__name__)


def hello_world(verbose: bool = False):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("Hello World")


if __name__ == "__main__":
    hello_world(verbose=True)
