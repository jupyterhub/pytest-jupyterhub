""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import asyncio
import sys

import pytest
from jupyterhub.spawner import Spawner
from jupyterhub.tests.mocking import MockHub
from traitlets.config import Config


@pytest.fixture
def spawner_class():
    """Allows tests to setup the Spawner class that will be used by the hub."""
    return Spawner


@pytest.fixture
def jupyterhub_spawner_class_config(spawner_class):
    """Configures JupyterHub to use the Spawner class specified in the spawner_class fixture."""
    spawner_class_config = {"JupyterHub": {"spawner_class": spawner_class}}
    return Config(spawner_class_config)


@pytest.fixture
def spawner_config():
    """Allows tests to setup configurations that are specific to the spawner implementation"""
    return Config()


@pytest.fixture
def app_for_spawners(request, jupyterhub_spawner_class_config, spawner_config):
    """Creates an instance of a JupyterHub application that can be used by different spawner implementation test suites"""
    config = jupyterhub_spawner_class_config.merge(spawner_config)

    mocked_app = MockHub.instance(config=config)

    async def make_app():
        """Initializes the mocked application and starts it"""
        await mocked_app.initialize([])
        await mocked_app.start()

    def fin():
        """Disconnects logging during cleanup because pytest closes captured FDs prematurely"""
        mocked_app.log.handlers = []
        MockHub.clear_instance()
        try:
            mocked_app.stop()
        except Exception as e:
            print("Error stopping Hub: %s" % e, file=sys.stderr)

    request.addfinalizer(fin)
    asyncio.run(make_app())
    return mocked_app
