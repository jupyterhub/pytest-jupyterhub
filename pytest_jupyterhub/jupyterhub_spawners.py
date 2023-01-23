""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import pytest
from jupyterhub.spawner import Spawner


@pytest.fixture
def spawner_class():
    """Allows tests to setup the Spawner class that will be used by the hub."""
    return Spawner
