# Reusable JupyterHub Pytest Plugin

## Description
This is a reusable pytest plugin for testing JupyterHub's components

**JupyterHub** is a modular and extensible project, with components, like the **proxy**, **authenticator** and **spawner**, that can be easily replaced with alternate implementations. Testing the functionality of these components against JupyterHub is important and it requires various hub setups that can sometimes become complicated.

Each of these hub components and the hub itself define their own testing infrastructure, building everything from the ground up using the **pytest** framework. And some of this complex work is either repetitive across JupyterHub sub-projects, or under-specified for some of them. This has sparked a need to abstract these common parts into a separate testing framework.

The goal is to provide importable testing utilities to make it easier for contributors to write tests for the various hub components.