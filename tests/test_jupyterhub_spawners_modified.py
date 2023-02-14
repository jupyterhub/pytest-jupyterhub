import pytest
from jupyterhub.app import JupyterHub
from jupyterhub.tests.mocking import MockSpawner
from traitlets.config import Config


@pytest.fixture
async def spawner_class():
    """Sets the MockSpawner class as the spawner to be used by the hub"""
    return MockSpawner


@pytest.fixture
async def spawner_config():
    """Sets the configuration attributes specific to the current spawner implementation"""
    spawner_config = {"MockSpawner": {"home_dir_template": "/tmp/Jeff"}}
    return Config(spawner_config)


async def test_jupyterhub_spawner_class_config(jupyterhub_spawner_class_config):
    """Tests that the jupyterhub_spawner_class_config returns the spawner class set by the spawner_class fixture"""
    assert jupyterhub_spawner_class_config["JupyterHub"]["spawner_class"] == MockSpawner


async def test_app_for_spawners(app_for_spawners):
    """Tests the app_for_spawners fixture"""
    assert isinstance(app_for_spawners, JupyterHub)
    assert app_for_spawners.spawner_class == MockSpawner
    assert app_for_spawners.config.MockSpawner.home_dir_template == "/tmp/Jeff"
