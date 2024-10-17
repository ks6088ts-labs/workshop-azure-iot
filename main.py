import logging

import typer
import uvicorn

from workshop_azure_iot.core import app as fastapi_app

app = typer.Typer()
logger = logging.getLogger(__name__)


@app.command()
def server(
    host="0.0.0.0",
    port: int = 8000,
    verbose: bool = False,
):
    uvicorn.run(
        app=fastapi_app,
        host=host,
        port=port,
        log_level=logging.DEBUG if verbose else logging.INFO,
    )


@app.command()
def sandbox(
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    logger.debug("debug")
    logger.warning("warning")


if __name__ == "__main__":
    app()
