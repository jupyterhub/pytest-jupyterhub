# Fixtures and Mocks of the `jupyterhub` package

(jupyterhub-mockhub)=

## [The MockHub Class](https://github.com/jupyterhub/jupyterhub/blob/e4f72c9eeb4cd308ff5cbcf21142b2cb0a0345e4/jupyterhub/tests/mocking.py#L220)

It is a subclass of `JupyterHub` that allows for easier testing of the `JupyterHub` class and other components that require a running instance of JupyterHub. It does this by providing [mock](https://docs.python.org/3/library/unittest.mock.html) implementations of specific functions of a JupyterHub instance, sometimes modified for testing purposes. For example, the `init_db` function initializes the MockHub database by first resetting it to a clean state before running tests, the `initialize` function initializes the MockHub application and adds an initial user to the database to run tests against, the `stop` function stops the MockHub application and performs any necessary cleanup of the testing environment etc

```{admonition} Example
The `conftest` module of the `DockerSpawner` repository imports and uses the JupyterHub `MockHub` class. This can be seen [here](https://github.com/jupyterhub/dockerspawner/blob/8503af69161a3a543cc613f93ce7951ad30a1912/tests/conftest.py#L26).

It sets the `hub_ip` and `hub_connect_ip` attributes of the mocked instance.
These attributes specify the IP addresses that the mock instance of JupyterHub will be listening in on and connecting to.
```

(jupyterhub-app-fixture)=

## [The App Fixture](https://github.com/jupyterhub/jupyterhub/blob/e4f72c9eeb4cd308ff5cbcf21142b2cb0a0345e4/jupyterhub/tests/conftest.py#L61)

The `app` [fixture](https://docs.pytest.org/en/latest/explanation/fixtures.html) is used to provide a lightweight, running `JupyterHub` application for testing. It is responsible for starting the mock `JupyterHub` application instance, the [MockHub](jupyterhub-mockhub) and stopping it after all tests in the module have been completed.

```{admonition} Example
The `conftest` module of the `DockerSpawner` repository imports and uses the JupyterHub `app` fixture. This can be seen [here](https://github.com/jupyterhub/dockerspawner/blob/8503af69161a3a543cc613f93ce7951ad30a1912/tests/conftest.py#L60).

It configures the mocked app instance to use the `DockerSpawner` class and its sub-classes: `SwarmSpawner` and `SystemUserSpawner`, to spawn single-user servers.
```

The `MockHub` class and the `app` fixture of the `JupyterHub` repository and the fixtures they rely on i.e: `event_loop`, `io_loop`, `ssl_tmpdir`, should be adapted for use in the **JupyterHub Pytest Plugin** to enable for testing of the DockerSpawner and other JupyterHub component implementations without having to import them from the JupyterHub repository.
