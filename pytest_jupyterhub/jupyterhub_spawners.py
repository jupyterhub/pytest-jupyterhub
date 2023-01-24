""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import pytest
from jupyterhub.spawner import Spawner
from traitlets.config import Config


@pytest.fixture
def spawner_class():
    """Allows tests to setup the Spawner class that will be used by the hub."""
    return Spawner


@pytest.fixture
def jupyterhub_spawner_config(spawner_class):
    """Configures JupyterHub to use the Spawner class"""
    c = Config()
    c.JupyterHub.spawner_class = spawner_class
    return c
