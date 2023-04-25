# Changelog

For detailed changes from the prior release, click on the version number, and
its link will bring up a GitHub listing of changes. Use `git log` on the command line for details.

## [0.1.0](https://github.com/jupyterhub/pytest-jupyterhub/compare/0a6ed6d634f8bd9ae294a367fad1757f521f18b1...0.1.0) 2023-04-25

First release!

### Enhancements made

- Setup codecov to track test coverage [#56](https://github.com/jupyterhub/pytest-jupyterhub/pull/56) ([@Sheila-nk](https://github.com/Sheila-nk))
- Create release workflow file [#48](https://github.com/jupyterhub/pytest-jupyterhub/pull/48) ([@Sheila-nk](https://github.com/Sheila-nk))
- Refactor fixtures, add some tests for them and run them with GitHub actions [#36](https://github.com/jupyterhub/pytest-jupyterhub/pull/36) ([@Sheila-nk](https://github.com/Sheila-nk))
- Configure sphinx to extract docstrings [#32](https://github.com/jupyterhub/pytest-jupyterhub/pull/32) ([@Sheila-nk](https://github.com/Sheila-nk))
- make all plugin fixtures async [#31](https://github.com/jupyterhub/pytest-jupyterhub/pull/31) ([@Sheila-nk](https://github.com/Sheila-nk))
- add fixture that creates an instance of JupyterHub [#28](https://github.com/jupyterhub/pytest-jupyterhub/pull/28) ([@Sheila-nk](https://github.com/Sheila-nk))
- Create fixture for spawner specific configurations [#24](https://github.com/jupyterhub/pytest-jupyterhub/pull/24) ([@Sheila-nk](https://github.com/Sheila-nk))
- Create fixture that configures JupyterHub to use the Spawner class [#23](https://github.com/jupyterhub/pytest-jupyterhub/pull/23) ([@Sheila-nk](https://github.com/Sheila-nk))
- Create a fixture returning the spawner class [#21](https://github.com/jupyterhub/pytest-jupyterhub/pull/21) ([@Sheila-nk](https://github.com/Sheila-nk))
- add initial app_for_spawners fixture [#19](https://github.com/jupyterhub/pytest-jupyterhub/pull/19) ([@Sheila-nk](https://github.com/Sheila-nk))
- Rename package to pytest-jupyterhub and change all occurrences of old package name [#17](https://github.com/jupyterhub/pytest-jupyterhub/pull/17) ([@Sheila-nk](https://github.com/Sheila-nk))
- Add the skeleton for an initial plugin for spawners and register it as a project entrypoint [#15](https://github.com/jupyterhub/pytest-jupyterhub/pull/15) ([@Sheila-nk](https://github.com/Sheila-nk))
- Add documents and packaging related files [#4](https://github.com/jupyterhub/pytest-jupyterhub/pull/4) ([@Sheila-nk](https://github.com/Sheila-nk))

### Maintenance and upkeep improvements

- Add RELEASE.md, and update release workflow to use PyPI's trusted publisher [#59](https://github.com/jupyterhub/pytest-jupyterhub/pull/59) ([@Sheila-nk](https://github.com/Sheila-nk))
- dependabot: monthly updates of github actions [#50](https://github.com/jupyterhub/pytest-jupyterhub/pull/50) ([@consideRatio](https://github.com/consideRatio))
- Create dependabot config file [#43](https://github.com/jupyterhub/pytest-jupyterhub/pull/43) ([@Sheila-nk](https://github.com/Sheila-nk))
- Add pre-commit config, flake8 config, enable autoflake [#18](https://github.com/jupyterhub/pytest-jupyterhub/pull/18) ([@GeorgianaElena](https://github.com/GeorgianaElena))

### Documentation improvements

- Add nodejs install instructions [#54](https://github.com/jupyterhub/pytest-jupyterhub/pull/54) ([@Sheila-nk](https://github.com/Sheila-nk))
- Add PyPI badge [#53](https://github.com/jupyterhub/pytest-jupyterhub/pull/53) ([@Sheila-nk](https://github.com/Sheila-nk))
- Add contributing instructions [#44](https://github.com/jupyterhub/pytest-jupyterhub/pull/44) ([@Sheila-nk](https://github.com/Sheila-nk))
- Update readme with Usage instructions [#39](https://github.com/jupyterhub/pytest-jupyterhub/pull/39) ([@Sheila-nk](https://github.com/Sheila-nk))
- add summary of JupyterHub MockHub class and App fixture [#12](https://github.com/jupyterhub/pytest-jupyterhub/pull/12) ([@Sheila-nk](https://github.com/Sheila-nk))
- update the docs directory [#11](https://github.com/jupyterhub/pytest-jupyterhub/pull/11) ([@Sheila-nk](https://github.com/Sheila-nk))
- add docs directory structure skeleton [#9](https://github.com/jupyterhub/pytest-jupyterhub/pull/9) ([@Sheila-nk](https://github.com/Sheila-nk))
- add readthedocs configuration file [#8](https://github.com/jupyterhub/pytest-jupyterhub/pull/8) ([@Sheila-nk](https://github.com/Sheila-nk))

### Continuous Integration

- pre-commit: bump isort [#29](https://github.com/jupyterhub/pytest-jupyterhub/pull/29) ([@Sheila-nk](https://github.com/Sheila-nk))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/pytest-jupyterhub/graphs/contributors?from=2022-12-12&to=2023-04-24&type=c))

[@consideRatio](https://github.com/search?q=repo%3Ajupyterhub%2Fpytest-jupyterhub+involves%3AconsideRatio+updated%3A2022-12-12..2023-04-24&type=Issues) | [@GeorgianaElena](https://github.com/search?q=repo%3Ajupyterhub%2Fpytest-jupyterhub+involves%3AGeorgianaElena+updated%3A2022-12-12..2023-04-24&type=Issues) | [@manics](https://github.com/search?q=repo%3Ajupyterhub%2Fpytest-jupyterhub+involves%3Amanics+updated%3A2022-12-12..2023-04-24&type=Issues) | [@minrk](https://github.com/search?q=repo%3Ajupyterhub%2Fpytest-jupyterhub+involves%3Aminrk+updated%3A2022-12-12..2023-04-24&type=Issues) | [@Sheila-nk](https://github.com/search?q=repo%3Ajupyterhub%2Fpytest-jupyterhub+involves%3ASheila-nk+updated%3A2022-12-12..2023-04-24&type=Issues)
