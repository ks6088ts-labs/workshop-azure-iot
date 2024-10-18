from logging import getLogger

import pytest

from tests.utilities import SKIP_TEST, client

logger = getLogger(__name__)


@pytest.mark.skipif(SKIP_TEST, reason="need to launch the backend server first")
def test_main():
    path_format = "/iot_hub{0}"
    response = client.get(
        url=path_format.format("/device_twin"),
    )
    assert response.status_code == 200
    logger.info(f"response: {response.json()}")
