(front-page)=

# Reusable Jupyterhub Pytest Plugin

The reusable Jupyterhub pytest plugin is essential for testing JupyterHub's components

JupyterHub is a modular and extensible project, with components, like the proxy, authenticator and spawner, that can be easily replaced with alternate implementations. Testing the functionality of these components against JupyterHub is important and it requires various hub setups that can sometimes become complicated.

Each of these hub components and the hub itself define their own testing infrastructure, building everything from the ground up using the pytest framework. And some of this complex work is either repetitive across JupyterHub sub-projects, or under-specified for some of them. This sparked a need to abstract these common parts into a separate testing framework.

The goal is to provide importable testing utilities to make it easier for contributors to write tests for the various hub components. This will involve creating and using **fixtures** and **mocks**.

## Contents

```{toctree}
:maxdepth: 2
:caption: Introduction
fixtures
```

```{toctree}
:maxdepth: 2
:caption: Plugins
plugins/index
```

```{toctree}
:maxdepth: 2
:caption: Contributing
contributing/index
```

```{toctree}
:maxdepth: 2
:caption: About JupyterHub Pytest Plugin
changelog
```

<!-- testing -->
<!-- packaging -->
<!-- misc -->
