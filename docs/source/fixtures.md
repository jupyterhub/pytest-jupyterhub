# Fixtures

## The JupyterHub MockHub Class
The `MockHub` class is a subclass of `JupyterHub`. It allows for easier testing of the `JupyterHub` class and other components that require a running instance of JupyterHub. It does this by providing mock implementations of particular functionality of a JupyterHub instance. It also allows for easier setup and cleanup of the testing environment.

To use the `MockHub` class, you would create an instance of it, and then call its methods or access its properties as needed.

**Example:**
```
mock_hub = MockHub()
mock_hub.initialize()
```
This would create a new `MockHub` instance and initialize it. You could then use the instance to perform various operations, such as adding users or starting servers, by calling methods on the instance.

## The JupyterHub App Fixture
The `app` fixture is used to provide a mock `JupyterHub` application instance for testing. The mock `JupyterHub` application instance is created using the `MockHub` class. The fixture is defined with `scope='module'`, meaning that it will be created once per test module and shared among all tests within the module. It takes a keyword argument `ssl_enabled`, which determines whether the mock `JupyterHub` application instance should be started with SSL enabled. It is also responsible for starting the mock `JupyterHub` application instance and stopping it after all tests in the module have been completed. 

The `app` fixture is used in a test module by including it as an argument in the test function or method. When the test function is executed, the `app` fixture will be called and the mock JupyterHub application instance will be passed as an argument to the test function. This allows the test function to use the mock JupyterHub application instance to perform assertions or other operations as part of the test.

**Example:**
```
def test_something(app):
    # Use the mock JupyterHub application instance to perform some operation
    result = app.do_something()
    
    # Assert that the result is as expected
    assert result == expected_result
```

## Their usage outside the JupyterHub repository
The `conftest` module of the `DockerSpawner` repository imports and uses the JupyterHub `MockHub` class. It sets the `hub_ip` and `hub_connect_ip` attributes of the mocked instance. These attributes specify the IP addresses that the mock instance of JupyterHub will be listening in on and connecting to.

The `conftest` module of the `DockerSpawner` repository also imports and uses the JupyterHub `app` fixture. It configures the mocked app instance to use the `DockerSpawner` class and its sub-classes: `SwarmSpawner` and `SystemUserSpawner`, to spawn single-user servers.

The `MockHub` class and the `app` fixture of the `JupyterHub` repository and the fixtures they rely on i.e: `event_loop`, `io_loop`, `ssl_tmpdir`, should be included in the **JupyterHub Pytest Plugin** to enable for testing of the DockerSpawner and other JupyterHub component implementations without having to import them from the JupyterHub repository.