""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import sys

import pytest
from jupyterhub.tests.mocking import MockHub, MockSpawner
from traitlets.config import Config


@pytest.fixture
async def get_configured_mockhub_instance():
    def _create_configured_mockhub_instance(
        config=Config(),
    ):
        MockHub.clear_instance()
        mocked_app = MockHub.instance(config=config)
        return mocked_app

    return _create_configured_mockhub_instance


@pytest.fixture
async def hub_app(hub_app_cleanup):
    app = MockHub.instance()
    await app.initialize([])
    await app.start()

    return app


@pytest.fixture()
def hub_app_cleanup():
    """Automatically cleans up hub resources."""
    yield
    app = MockHub.instance()
    app.log.handlers = []
    try:
        app.stop()
    except Exception as e:
        print("Error stopping Hub: %s" % e, file=sys.stderr)

    MockHub.clear_instance()
