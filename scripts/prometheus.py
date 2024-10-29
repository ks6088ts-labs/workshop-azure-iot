import logging
import math
import time

import typer
from prometheus_client import Gauge, start_http_server

app = typer.Typer()
logger = logging.getLogger(__name__)


class Simulator:
    def __init__(self, name="simulator"):
        self.temperature = Gauge(f"{name}_temperature", f"Temperature for {name}")

    def update(self, t):
        self.temperature.set(20 + 5 * math.sin(t))


@app.command()
def run(
    num_devices: int = 3,
    port: int = 8000,
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    logger.info(f"Running {num_devices} simulators on port {port}")
    devices = [Simulator(name=f"simulator{i:03d}") for i in range(num_devices)]

    start_http_server(port)

    while True:
        time.sleep(1)
        t = time.time()
        for idx, device in enumerate(devices):
            value = t + idx * 0.1
            device.update(t=value)
            logger.info(f"Device {idx} updated to {value}")


if __name__ == "__main__":
    app()
