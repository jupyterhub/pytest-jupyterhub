""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import sys

import pytest
from jupyterhub.tests.mocking import MockHub
from traitlets.config import Config


@pytest.fixture
async def get_configured_mockhub_instance():
    """
    Creates a MockHub instance from a provided traitlets.config Config object
    or the empty Config is none is passed as an argument.

    This fixture is a factory and returns a function.
    More about factory fixtures at https://docs.pytest.org/en/latest/how-to/fixtures.html#factories-as-fixtures

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
async def hub_app():
    """
    Starts and yields the existing global instance of MockHub.
    The app is stopped and the instance is cleaned up afterwards.
    """
    # Get the global instance of MockHub
    # ref: https://traitlets.readthedocs.io/en/stable/config-api.html#traitlets.config.SingletonConfigurable.instance
    app = MockHub.instance()
    await app.initialize([])
    await app.start()

    yield app

    app.log.handlers = []
    try:
        # Explicitly close the http server socket to not leek any fds
        # Also await app.shutdown_cancel_tasks()
        # Note that this is equivalent to the app.stop() function
        # Explicitly cleaning up resources like this, removes the need to depend
        # on the io_loop fixture to make sure the cleanup happens before the io_loop is closed.
        # ref https://github.com/jupyterhub/jupyterhub/blob/c9d52ce6ffd255c26b6ecd396a81583a7250c53b/jupyterhub/app.py#L3356-L3358
        if app.http_server:
            app.http_server.stop()
        await app.shutdown_cancel_tasks()
    except Exception as e:
        print("Error stopping Hub: %s" % e, file=sys.stderr)

    MockHub.clear_instance()
