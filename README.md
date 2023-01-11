# Reusable JupyterHub Pytest Plugin

## Description
This is a reusable pytest plugin for testing JupyterHub's components

**JupyterHub** is a modular and extensible project, with components, like the **proxy**, **authenticator** and **spawner**, that can be easily replaced with alternate implementations. Testing the functionality of these components against JupyterHub is important and it requires various hub setups that can sometimes become complicated.

Each of these hub components and the hub itself define their own testing infrastructure, building everything from the ground up using the **pytest** framework. And some of this complex work is either repetitive across JupyterHub sub-projects, or under-specified for some of them. This has sparked a need to abstract these common parts into a separate testing framework.

The goal is to provide importable testing utilities to make it easier for contributors to write tests for the various hub components.
This will involve creating and using **fixtures** and **mocks**.

A **Fixture** is a function that is used to prepare and clean up the environment for a test function. Fixtures can be used to set up test data, test environment, and other resources that are needed by test functions.
For more information on Fixtures, check out this [pytest documentation](https://docs.pytest.org/en/latest/explanation/fixtures.html) on fixtures.

A **Mock** is an object that simulates the behavior of another object such as a class or function. They are used to simulate the behavior of real objects for testing purposes.
For more information on Mocks, check out this [unittest documentation](https://docs.python.org/3/library/unittest.mock.html) on the mock module.

**Example:**

The [init_db](https://github.com/jupyterhub/jupyterhub/blob/336d7cfcfaf74087e4ee467d5e3d3bec0c25c3d0/jupyterhub/app.py#L1804) function in JupyterHub's `app` module initializes a connection to a database using SQLAlchemy's ORM (Object-Relational Mapper).

However, the mock [init_db](https://github.com/jupyterhub/jupyterhub/blob/336d7cfcfaf74087e4ee467d5e3d3bec0c25c3d0/jupyterhub/tests/mocking.py#L295) function in JupyterHub's `mocking` module initializes a database connection for the mocked JupyterHub application instance by calling the `init_db` function of the JupyterHub superclass but also has a `test_clean_db` attribute to ensure that the database is reset to a clean state before running tests.