from jupyterhub.app import JupyterHub
from jupyterhub.spawner import Spawner


async def test_spawner_class(spawner_class):
    """Tests that the spawner_class fixture returns class Spawner"""
    assert spawner_class == Spawner


async def test_spawner_config(spawner_config):
    """Tests that the spawner_config fixture returns an empty config"""
    assert spawner_config == {}


async def test_jupyterhub_spawner_class_config(jupyterhub_spawner_class_config):
    """Tests that the jupyterhub_spawner_class_config returns the class returned by spawner_class fixture"""
    assert jupyterhub_spawner_class_config["JupyterHub"]["spawner_class"] == Spawner


async def test_app_for_spawners(app_for_spawners):
    """Tests that the app fixture is an instance of JupyterHub"""
    assert isinstance(app_for_spawners, JupyterHub)
