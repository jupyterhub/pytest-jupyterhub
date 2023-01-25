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
def jupyterhub_spawner_class_config(spawner_class):
    """Configures JupyterHub to use the Spawner class specified in the spawner_class fixture."""
    spawner_class_config = {"JupyterHub": {"spawner_class": spawner_class}}
    return Config(spawner_class_config)


@pytest.fixture
def spawner_config():
    """Allows tests to setup configurations that are specific to the spawner implementation"""
    spawner_config = {}
    return Config(spawner_config)
