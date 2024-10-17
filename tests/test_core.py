from logging import getLogger

from tests.utilities import client

logger = getLogger(__name__)


def test_core():
    path_format = "/core/{0}"
    response = client.get(
        url=path_format.format("info"),
    )
    assert response.status_code == 200
    logger.info(f"response: {response.json()}")
