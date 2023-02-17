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

    # Check defaults
    assert hub_instance.spawner_class == MockSpawner
    assert not hub_instance.config
    assert not hub_instance.pid_file


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

    # Check expected config
    assert new_hub_instance.spawner_class == config_dict["JupyterHub"]["spawner_class"]
    assert new_hub_instance.config == config_dict

    # No `pid_file` should be available for a simple non-running hub instance
    assert not new_hub_instance.pid_file


async def test_default_hub_app(hub_app):
    """
    Tests that the `hub_app` factory fixture creates a new instance of a MockHub
    with no overriding config and the app was started.
    """
    app = await hub_app()
    assert isinstance(app, JupyterHub)

    # Check defaults
    assert app.spawner_class == MockSpawner
    assert not app.config

    # When the app is initialized, a `pid_file` should be created.
    assert app.pid_file


async def test_hub_app_configured(hub_app):
    """
    Tests that the `hub_app` factory fixture creates a new instance of a MockHub
    using a provided config dict and that the app was started.
    """
    config_dict = {
        "JupyterHub": {"spawner_class": Spawner},
        "Spawner": {"temp_dir": "/tmp/geo"},
    }
    app = await hub_app(config_dict)

    # Check expected config
    assert app.spawner_class == config_dict["JupyterHub"]["spawner_class"]
    assert app.config == config_dict

    # When the app is initialized, a `pid_file` should be created.
    assert app.pid_file
