""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import sys

import pytest
from jupyterhub.tests.mocking import MockHub
from traitlets.config import Config


@pytest.fixture
async def configured_mockhub_instance():
    """
    Creates a MockHub instance from a provided config dict
    or with the empty config if none is passed as an argument.

    This fixture is a factory and returns a function.
    More about factory fixtures at https://docs.pytest.org/en/latest/how-to/fixtures.html#factories-as-fixtures

    It should be called like:
    .. code-block:: python

        def my_test(configured_mockhub_instance):
            hub_instance = configured_mockhub_instance(config={"a": "b"})
            ...

    Note that the fixture has a `function` scope.
    """

    def _create_configured_mockhub_instance(
        config={},
    ):
        MockHub.clear_instance()
        mocked_app = MockHub.instance(config=Config(config))
        return mocked_app

    return _create_configured_mockhub_instance


@pytest.fixture
async def hub_app(configured_mockhub_instance):
    """
    Creates a MockHub instance from a provided config dict, it then
    starts and yields it.

    This fixture is a factory and returns an async function.
    More about factory fixtures at https://docs.pytest.org/en/latest/how-to/fixtures.html#factories-as-fixtures

    It should be called like:
    .. code-block:: python

        async def my_test(hub_app):
            app = await hub_app(config={"a": "b"})
            ...

    The created app is stopped and the instance is cleaned up afterwards.

    Note that the fixture has a `function` scope.
    """

    async def _create_hub_app(config={}):
        # Get the global instance of MockHub
        # ref: https://traitlets.readthedocs.io/en/stable/config-api.html#traitlets.config.SingletonConfigurable.instance
        app = configured_mockhub_instance(config)
        await app.initialize()
        await app.start()

        return app

    yield _create_hub_app

    app = MockHub.instance()
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
