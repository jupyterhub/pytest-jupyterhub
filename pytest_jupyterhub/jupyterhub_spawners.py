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
    """
    Creates a MockHub instance from a provided traitlets.config Config object
    or the empty Config is none is passed as an argument.

    This fixture is a factory and returns a function.

    It should be called like:
    .. code-block:: python
      def my_test(get_configured_mockhub_instance):
         hub_instance = get_configured_mockhub_instance(config=Config({"a": "b"})
         ...
    """
    def _create_configured_mockhub_instance(
        config=Config(),
    ):
        MockHub.clear_instance()
        mocked_app = MockHub.instance(config=config)
        return mocked_app

    return _create_configured_mockhub_instance


@pytest.fixture
async def hub_app(hub_app_cleanup):
    """
    Starts the current hub app.
    """
    # Get the global instance of MockHub
    # ref: https://traitlets.readthedocs.io/en/stable/config-api.html#traitlets.config.SingletonConfigurable.instance
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
