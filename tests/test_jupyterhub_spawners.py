from jupyterhub.app import JupyterHub
from jupyterhub.spawner import Spawner
from jupyterhub.tests.mocking import MockSpawner


async def test_default_mockhub_instance_creator(configured_mockhub_instance):
    """
    Tests that the `configured_mockhub_instance` factory fixture creates a new instance of a MockHub
    with no overriding config.
    """
    hub_instance = configured_mockhub_instance()
    assert isinstance(hub_instance, JupyterHub)
    assert hub_instance.spawner_class == MockSpawner
    assert hub_instance.config == {}


async def test_mockhub_instance_creator(configured_mockhub_instance):
    """
    Tests that the `configured_mockhub_instance` factory fixture creates a new instance of a MockHub
    using a provided config dict.
    """
    config_dict = {
        "JupyterHub": {"spawner_class": Spawner},
        "Spawner": {"home_dir_template": "/tmp/Jeff"},
    }
    new_hub_instance = configured_mockhub_instance(config_dict)
    assert isinstance(new_hub_instance, JupyterHub)
    assert new_hub_instance.spawner_class == config_dict["JupyterHub"]["spawner_class"]
    assert new_hub_instance.config == config_dict


async def test_default_hub_app(hub_app):
    """
    Tests that the `hub_app` factory fixture creates a new instance of a MockHub
    with no overriding config.
    """
    app = await hub_app()
    assert isinstance(app, JupyterHub)
    assert app.spawner_class == MockSpawner
    assert app.config == {}


async def test_hub_app_configured(hub_app):
    config_dict = {
        "JupyterHub": {"spawner_class": Spawner},
        "Spawner": {"temp_dir": "/tmp/geo"},
    }
    app = await hub_app(config_dict)
    assert app.spawner_class == config_dict["JupyterHub"]["spawner_class"]
    assert app.config == config_dict
