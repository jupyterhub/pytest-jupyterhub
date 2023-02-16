from traitlets.config import Config

from jupyterhub.app import JupyterHub
from jupyterhub.spawner import Spawner
from jupyterhub.tests.mocking import MockSpawner

async def test_default_mockhub_instance_creator(get_configured_mockhub_instance):
    hub_instance = get_configured_mockhub_instance()
    assert isinstance(hub_instance, JupyterHub)
    assert hub_instance.spawner_class == MockSpawner
    assert hub_instance.config == {}


async def test_default_hub_app(hub_app):
    assert isinstance(hub_app, JupyterHub)
    assert hub_app.spawner_class == MockSpawner


async def test_mockhub_instance_creator(get_configured_mockhub_instance):
    config_dict = {
        "JupyterHub": {"spawner_class": Spawner},
        "Spawner": {"home_dir_template": "/tmp/Jeff"},
    }
    new_hub_instance = get_configured_mockhub_instance(config=Config(config_dict))
    assert isinstance(new_hub_instance, JupyterHub)
    assert new_hub_instance.spawner_class == config_dict["JupyterHub"]["spawner_class"]
    assert new_hub_instance.config == config_dict


async def test_hub_app(hub_app):
    assert isinstance(hub_app, JupyterHub)
    config_dict = {
        "JupyterHub": {"spawner_class": Spawner},
        "Spawner": {"home_dir_template": "/tmp/Jeff"},
    }
    assert hub_app.spawner_class == config_dict["JupyterHub"]["spawner_class"]
    assert hub_app.config == config_dict
