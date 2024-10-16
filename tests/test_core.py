import logging

from template_python.core import hello_world


def test_hello_world_verbose(caplog):
    with caplog.at_level(logging.DEBUG):
        hello_world(verbose=True)
    assert "Hello World" in caplog.text


def test_hello_world_non_verbose(caplog):
    with caplog.at_level(logging.DEBUG):
        hello_world(verbose=False)
    assert "Hello, world!" not in caplog.text
