from logging import getLogger

import pytest

from tests.utilities import SKIP_TEST, client

logger = getLogger(__name__)


@pytest.mark.skipif(SKIP_TEST, reason="need to launch the backend server first")
def test_ai_services():
    path_format = "/ai_services/{0}"
    response = client.post(
        url=path_format.format("chat/completions"),
        params={
            "prompt": "Hello, how are you?",
        },
        json={},
    )
    assert response.status_code == 200
    logger.info(f"response: {response.json()}")
