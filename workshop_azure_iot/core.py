import logging
from os import getenv

from fastapi import FastAPI

logger = logging.getLogger(__name__)
app = FastAPI(
    docs_url="/",
)


@app.get("/info")
def read_root():
    return {
        "version": getenv("VERSION", "0.0.0"),
    }


def hello_world(verbose: bool = False):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("Hello World")


if __name__ == "__main__":
    hello_world(verbose=True)
