from logging import getLogger

import pytest

from tests.utilities import SKIP_TEST, client

logger = getLogger(__name__)


@pytest.mark.skipif(SKIP_TEST, reason="need to launch the backend server first")
def test_main():
    path_format = "/blob_storage{0}"

    # list_images
    response = client.get(
        url=path_format.format("/images"),
    )
    assert response.status_code == 200
    logger.info(f"response: {response.json()}")
