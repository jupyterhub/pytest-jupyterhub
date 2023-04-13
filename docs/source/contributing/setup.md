(contributing/setup)=

# Setting up a development install

## System Requirements

The [JupyterHub Pytest Plugin](https://github.com/jupyterhub/pytest-jupyterhub) uses [JupyterHub](https://github.com/jupyterhub/jupyterhub) which can only run on macOS or Linux operating systems. If you are using Windows, we recommend using [VirtualBox](https://virtualbox.org) or a similar system to run [Ubuntu Linux](https://ubuntu.com) for development.

### Install Python

The JupyterHub Pytest Plugin is written in the [Python](https://python.org) programming language and requires you have at least version 3.8 installed locally. If you haven’t installed Python before, the recommended way to install it is to use [Miniforge](https://github.com/conda-forge/miniforge#download).

### Install nodejs

[NodeJS 12+](https://nodejs.org/en/) is required for building some JavaScript components. `configurable-http-proxy`, the default proxy implementation for JupyterHub, is written in Javascript. If you have not installed NodeJS before, we recommend installing it in the `miniconda` environment you set up for Python. You can do so with `conda install nodejs`.

Many in the Jupyter community use \[`nvm`\](<https://github.com/nvm-sh/nvm>) to managing node dependencies.

### Install git

The JupyterHub Pytest Plugin uses [Git](https://git-scm.com) & [GitHub](https://github.com) for development & collaboration. You need to [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to work on the JupyterHub Pytest Plugin. We also recommend getting a free account on GitHub.com.

## Setting up a development install

When developing Pytest JupyterHub, you would need to make changes and be able to instantly test the changes. To achieve that, a developer install is required.

:::{note}
This guide does not attempt to dictate _how_ development
environments should be isolated since that is a personal preference and can
be achieved in many ways, for example, `tox`, `conda`, `docker`, etc. See this
[forum thread](https://discourse.jupyter.org/t/thoughts-on-using-tox/3497) for
a more detailed discussion.
:::

1. Clone the [Pytest JupyterHub](https://github.com/jupyterhub/pytest-jupyterhub) repository to your computer.

   ```bash
   git clone https://github.com/jupyterhub/pytest-jupyterhub.git
   cd pytest-jupyterhub
   ```

2. Make sure the `python` and `npm` you installed are available to you on the command line.

   ```bash
   python -V
   ```

   This should return a version number greater than or equal to 3.8.

   ```bash
   npm -v
   ```

   This should return a version number greater than or equal to 5.0.

3. Install `configurable-http-proxy` (required to run and test the default JupyterHub configuration):

   ```bash
   npm install -g configurable-http-proxy
   ```

   If you get an error that says `Error: EACCES: permission denied`, you might need to prefix the command with `sudo`.
   `sudo` may be required to perform a system-wide install.
   If you do not have access to sudo, you may instead run the following commands:

   ```bash
   npm install configurable-http-proxy
   export PATH=$PATH:$(pwd)/node_modules/.bin
   ```

   The second line needs to be run every time you open a new terminal.

   If you are using conda you can instead run:

   ```bash
   conda install configurable-http-proxy
   ```

4. Install an editable version of Pytest-JupyterHub and its requirements for development and testing.

   ```bash
   python3 -m pip install --editable ".[test]"
   ```

5. You are now good to go! Run the tests to confirm all required dependencies have been installed correctly.

   ```bash
   pytest -v --cov=pytest_jupyterhub tests
   ```

Happy Coding! :)
