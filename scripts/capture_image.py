import logging

import cv2
import typer

app = typer.Typer()
logger = logging.getLogger(__name__)


def capture_image_from_file(filename: str) -> bytes:
    camera = cv2.VideoCapture(filename=filename)
    return_value, image = camera.read()
    del camera
    if not return_value:
        raise Exception("Error capturing image")
    return cv2.imencode(".jpg", image)[1].tobytes()


def capture_image_from_camera(index: int) -> bytes:
    camera = cv2.VideoCapture(index=index)
    import time

    time.sleep(2)  # FIXME: Warm-up time
    return_value, image = camera.read()
    del camera
    if not return_value:
        raise Exception("Error capturing image")
    return cv2.imencode(".jpg", image)[1].tobytes()


@app.command()
def file(
    filename: str = typer.Option("video.mp4", help="Path to the video file."),
    outfile: str = typer.Option("output.jpg", help="Output file name."),
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    data = capture_image_from_file(filename=filename)

    with open(outfile, "wb") as f:
        f.write(data)


@app.command()
def camera(
    index: int = typer.Option(0, help="Camera index."),
    outfile: str = typer.Option("output.jpg", help="Output file name."),
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    data = capture_image_from_camera(index=index)

    with open(outfile, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    app()
