# Fixtures and Mocks
A **Fixture** is a function that is used to prepare and clean up the environment for a test function. Fixtures can be used to set up test data, test environment, and other resources that are needed by test functions.
For more information, check out this [pytest documentation](https://docs.pytest.org/en/latest/explanation/fixtures.html) on fixtures.

A **Mock** is an object that simulates the behavior of another object such as a class or function. They are used to simulate the behavior of real objects for testing purposes.
For more information on Mocks, check out this [unittest documentation](https://docs.python.org/3/library/unittest.mock.html) on the mock module.
```{admonition} Example
The [init_db](https://github.com/jupyterhub/jupyterhub/blob/336d7cfcfaf74087e4ee467d5e3d3bec0c25c3d0/jupyterhub/app.py#L1804) function in JupyterHub's `app` module initializes a connection to a database using SQLAlchemy's ORM (Object-Relational Mapper).
However, the mock [init_db](https://github.com/jupyterhub/jupyterhub/blob/336d7cfcfaf74087e4ee467d5e3d3bec0c25c3d0/jupyterhub/tests/mocking.py#L295) function in JupyterHub's `mocking` module initializes a database connection for the mocked JupyterHub application instance by calling the `init_db` function of the JupyterHub superclass but also has a `test_clean_db` attribute to ensure that the database is reset to a clean state before running tests.
```

## [The MockHub Class](https://github.com/jupyterhub/jupyterhub/blob/e4f72c9eeb4cd308ff5cbcf21142b2cb0a0345e4/jupyterhub/tests/mocking.py#L220) 
It is a subclass of `JupyterHub` that allows for easier testing of the `JupyterHub` class and other components that require a running instance of JupyterHub. It does this by providing mock implementations of particular functionality of a JupyterHub instance. It also allows for easier setup and cleanup of the testing environment.
```{admonition} Example
The `conftest` module of the `DockerSpawner` repository imports and uses the JupyterHub `MockHub` class. This can be seen [here](https://github.com/jupyterhub/dockerspawner/blob/8503af69161a3a543cc613f93ce7951ad30a1912/tests/conftest.py#L26).

It sets the `hub_ip` and `hub_connect_ip` attributes of the mocked instance.
These attributes specify the IP addresses that the mock instance of JupyterHub will be listening in on and connecting to.
```

## [The App Fixture](https://github.com/jupyterhub/jupyterhub/blob/e4f72c9eeb4cd308ff5cbcf21142b2cb0a0345e4/jupyterhub/tests/conftest.py#L61)
It is used to provide a mock `JupyterHub` application instance for testing. It is also responsible for starting the mock `JupyterHub` application instance and stopping it after all tests in the module have been completed.
```{admonition} Example
The `conftest` module of the `DockerSpawner` repository imports and uses the JupyterHub `app` fixture. This can be seen [here](https://github.com/jupyterhub/dockerspawner/blob/8503af69161a3a543cc613f93ce7951ad30a1912/tests/conftest.py#L60).

It configures the mocked app instance to use the `DockerSpawner` class and its sub-classes: `SwarmSpawner` and `SystemUserSpawner`, to spawn single-user servers.
```

The `MockHub` class and the `app` fixture of the `JupyterHub` repository and the fixtures they rely on i.e: `event_loop`, `io_loop`, `ssl_tmpdir`, should be included in the **JupyterHub Pytest Plugin** to enable for testing of the DockerSpawner and other JupyterHub component implementations without having to import them from the JupyterHub repository.