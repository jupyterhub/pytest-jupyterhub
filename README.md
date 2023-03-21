**[Description](#description)** |
**[Installation](#installation)** |
**[Usage](#usage)**

---

# [Reusable JupyterHub Pytest Plugin](https://github.com/jupyterhub/pytest-jupyterhub)

[![Latest PyPI version](https://img.shields.io/pypi/v/pytest-jupyterhub?logo=pypi)](https://pypi.python.org/pypi/pytest-jupyterhub)
[![Documentation status](https://img.shields.io/readthedocs/pytest-jupyterhub?logo=read-the-docs)](https://pytest-jupyterhub.readthedocs.io/en/latest/?badge=latest)
[![GitHub Workflow Status - Test](https://github.com/jupyterhub/pytest-jupyterhub/actions/workflows/test.yml/badge.svg)](https://github.com/jupyterhub/pytest-jupyterhub/actions)
[![Test coverage of code](https://codecov.io/gh/jupyterhub/pytest-jupyterhub/branch/main/graph/badge.svg)](https://codecov.io/gh/jupyterhub/pytest-jupyterhub)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/pytest-jupyterhub/issues)

## Description

This is a reusable pytest plugin for testing JupyterHub's components

[**JupyterHub**](https://github.com/jupyterhub/jupyterhub) is a modular and extensible project, with components, like the **proxy**, **authenticator** and **spawner**, that can be easily replaced with alternate implementations. Testing the functionality of these components against JupyterHub is important and it requires various hub setups that can sometimes become complicated.

Each of these hub components and the hub itself define their own testing infrastructure, building everything from the ground up using the [**pytest**](https://docs.pytest.org/en/7.2.x/) framework. And some of this complex work is either repetitive across JupyterHub sub-projects, or under-specified for some of them. This has sparked a need to abstract these common parts into a separate testing framework.

The goal is to provide importable testing utilities to make it easier for contributors to write tests for the various hub components.
This will involve creating and using **fixtures** and **mocks**.

A **Fixture** is a function that is used to prepare and clean up the environment for a test function. Fixtures can be used to set up test data, test environment, and other resources that are needed by test functions.
For more information on Fixtures, check out this [pytest documentation](https://docs.pytest.org/en/latest/explanation/fixtures.html) on fixtures.

A **Mock** is an object that simulates the behavior of another object such as a class or function. They are used to simulate the behavior of real objects for testing purposes.
For more information on Mocks, check out this [unittest documentation](https://docs.python.org/3/library/unittest.mock.html) on the mock module.

### Example

The [init_db](https://github.com/jupyterhub/jupyterhub/blob/336d7cfcfaf74087e4ee467d5e3d3bec0c25c3d0/jupyterhub/app.py#L1804) function in JupyterHub's `app` module initializes a connection to a database using SQLAlchemy's ORM (Object-Relational Mapper).

However, the mock [init_db](https://github.com/jupyterhub/jupyterhub/blob/336d7cfcfaf74087e4ee467d5e3d3bec0c25c3d0/jupyterhub/tests/mocking.py#L295) function in JupyterHub's `mocking` module initializes a database connection for the mocked JupyterHub application instance by calling the `init_db` function of the JupyterHub superclass but also has a `test_clean_db` attribute to ensure that the database is reset to a clean state before running tests.

## Installation

To use the **JupyterHub Pytest Plugin**, you will first need to install it using pip by either:

- installing it locally
  ```bash
  pip install --upgrade pip
  pip install git+https://github.com/jupyterhub/pytest-jupyterhub.git@main
  ```
- adding it to the `requirements.txt` file of your project:

  ```python
  # in requirements.txt
  git+https://github.com/jupyterhub/pytest-jupyterhub.git@main
  ```

  then run:

  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

## Usage

To use a specific fixture or mock, import it from its module in the `pytest_jupyterhub` package:

```python
from pytest_jupyterhub.jupyterhub_spawners import hub_app
```

### Example

The [`hub_app` fixture](https://github.com/jupyterhub/pytest-jupyterhub/blob/829aad654cb69de56b227c7177a844a0b5ea8485/pytest_jupyterhub/jupyterhub_spawners.py#L42) is a [factory fixture](https://docs.pytest.org/en/latest/how-to/fixtures.html#factories-as-fixtures) that creates a `MockHub` instance from a provided `config` dictionary defining spawner-specific attribute configurations. It then yields the mocked instance. After testing, the running hub instance is stopped and a cleanup is performed.

An illustration of its integration within the [`DockerSpawner` test suite](https://github.com/jupyterhub/dockerspawner/blob/af2da8d06898406816193f7a68b21b776fc909b6/tests/conftest.py#L71) is provided below:

```python
@pytest.fixture
async def app(hub_app):
    config = {
        "Dockerspawner": {
            "prefix": "dockerspawner-test"
        }
    }

    if len(jh_version_info) > 3 and jh_version_info[3]:
        tag = jupyterhub.__version__
        config["Dockerspawner"]["image"] = f"jupyterhub/singleuser:{tag}"

    app = await hub_app(config=config)

    return app
```
