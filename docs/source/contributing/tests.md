(contributing-tests)=

# Testing Pytest JupyterHub and Linting code

Unit testing helps to validate that Pytest JupyterHub works the way we think it does, and continues to do so when changes occur. They also help communicate
precisely what we expect our code to do.

Pytest JupyterHub uses [pytest](https://pytest.org) for all the tests. You can find them under the [pytest-jupyterhub/tests](https://github.com/jupyterhub/pytest-jupyterhub/tree/main/tests) directory in the git repository.

## Running the tests

1. Make sure you have completed {ref}`contributing/setup`.

2. You can run all tests in Pytest JupyterHub

   ```bash
   pytest -v tests
   ```

   This should display progress as it runs all the tests, printing information about any test failures as they occur.

3. You can also run tests in just a specific file:

   ```bash
   pytest -v tests/<test-file-name>
   ```

4. To run a specific test only, you can do:

   ```bash
   pytest -v tests/<test-file-name>::<test-name>
   ```

   This runs the test with function name `<test-name>` defined in `<test-file-name>`. This is very useful when you are iteratively developing a single test.

   For example, to run the test `test_default_hub_app` in the file `test_jupyterhub_spawners.py`, you would run:

   ```bash
   pytest -v tests/test_jupyterhub_spawners.py::test_default_hub_app
   ```

   For more details, refer to the [pytest usage documentation](https://pytest.readthedocs.io/en/latest/usage.html).

### The Pytest-Asyncio Plugin

When testing the various JupyterHub components and their various implementations, it sometimes becomes necessary to have a running instance of JupyterHub to test against.
The [`app`](https://github.com/jupyterhub/jupyterhub/blob/270b61992143b29af8c2fab90c4ed32f2f6fe209/jupyterhub/tests/conftest.py#L60) fixture mocks a JupyterHub application for use in testing by:

- enabling ssl if internal certificates are available
- creating an instance of [MockHub](https://github.com/jupyterhub/jupyterhub/blob/270b61992143b29af8c2fab90c4ed32f2f6fe209/jupyterhub/tests/mocking.py#L221) using any provided configurations as arguments
- initializing the mocked instance
- starting the mocked instance
- finally, a registered finalizer function performs a cleanup and stops the mocked instance

The JupyterHub test suite uses the [pytest-asyncio plugin](https://pytest-asyncio.readthedocs.io/en/latest/) that handles [event-loop](https://docs.python.org/3/library/asyncio-eventloop.html) integration in [Tornado](https://www.tornadoweb.org/en/stable/) applications. This allows for the use of top-level awaits when calling async functions or [fixtures](https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are) during testing. All test functions and fixtures labelled as `async` will run on the same event loop.

```{note}
With the introduction of [top-level awaits](https://piccolo-orm.com/blog/top-level-await-in-python/), the use of the `io_loop` fixture of the [pytest-tornado plugin](https://www.tornadoweb.org/en/stable/ioloop.html) is no longer necessary. It was initially used to call coroutines. With the upgrades made to `pytest-asyncio`, this usage is now deprecated. It is now, only utilized within the JupyterHub test suite to ensure complete cleanup of resources used during testing such as open file descriptors. This is demonstrated in this [pull request](https://github.com/jupyterhub/jupyterhub/pull/4332).
More information is provided below.
```

One of the general goals of the [JupyterHub Pytest Plugin project](https://github.com/jupyterhub/pytest-jupyterhub) is to ensure the MockHub cleanup fully closes and stops all utilized resources during testing so the use of the `io_loop` fixture for teardown is not necessary. This was highlighted in this [issue](https://github.com/jupyterhub/pytest-jupyterhub/issues/30)

For more information on asyncio and event-loops, here are some resources:

- **Read**: [Introduction to the Python event loop](https://www.pythontutorial.net/python-concurrency/python-event-loop)
- **Read**: [Overview of Async IO in Python 3.7](https://stackabuse.com/overview-of-async-io-in-python-3-7)
- **Watch**: [Asyncio: Understanding Async / Await in Python](https://www.youtube.com/watch?v=bs9tlDFWWdQ)
- **Watch**: [Learn Python's AsyncIO #2 - The Event Loop](https://www.youtube.com/watch?v=E7Yn5biBZ58)

## Troubleshooting Test Failures

### All the tests are failing

Make sure you have completed all the steps in {ref}`contributing/setup` successfully.

## Code formatting and linting

Pytest JupyterHub automatically enforces code formatting. This means that pull requests with changes breaking this formatting will receive a commit from `pre-commit.ci` automatically.

To automatically format code locally, you can install `pre-commit` and register a _git hook_ to automatically check with pre-commit before you make a commit if the formatting is okay.

```bash
pip install pre-commit
pre-commit install --install-hooks
```

To run pre-commit manually you would do:

```bash
# check for changes to code not yet committed
pre-commit run

# check for changes also in already committed code
pre-commit run --all-files
```

To skip pre-commit checks use the tag `--no-verify` in your commit.

```bash
git commit -m "initial commit" --no-verify
```

You may also install [black integration](https://github.com/psf/black#editor-integration) into your text editor to format code automatically.
