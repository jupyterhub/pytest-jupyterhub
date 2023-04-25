# How to make a release

`pytest-jupyterhub` is a package available on [PyPI].

These are the instructions on how to make a release.

## Pre-requisites

- Push rights to this GitHub repository

## Steps to make a release

1. Create a PR updating `docs/source/changelog.md` with [github-activity] and
   continue to step 2 **only when its merged.**

   Tips about getting the most out of github-activity (from https://github.com/jupyterhub/team-compass/issues/563):

   - [ ] Run `github-activity --heading-level=3`
   - [ ] Consider labelling PRs:
     - Read the output of `github-activity` and look for PRs under the uncategorized heading
       that didn't have a label for `github-activity` to sort it by.
     - If any non-bot authored PRs are found there, visit them and add a relevant label.
     - `github-activity` can't sort `ci` labels automatically to go under a `### Continuous integration` improvements heading,
       so these need ot handeled manually.
   - [ ] Cosider updating PR title:
     - Read the output of `github-activity` and look for PRs with a title that can be improved,
       then update the title of the PR on GitHub.
   - [ ] Run `github-activity --heading-level=3` (again),
         copy and paste the output of `github-activity` to the changelog and refine it manually:
     - Decide a version increment.
       - Bump major version if a breaking change is introduced
         If a major version bump is made, also write some summary manually before listing all the PRs.
       - Bump minor version if an enhancement or new feature is added
       - Bump patch version if only documentation and bugfixes etc are provided.
     - Add a date to the release that seems likely to match when it can get merged
     - Remove various pre-commit PRs and dependabot PRs that just bumps CI stuff.
     - Remove various @welcome, @dependabot, and other bots from contributors lists etc
     - Put ci labelled PRs manually under `### Continuous integration` improvements heading
   - [ ] Make a commit with a message similar to _"Add changelog for 1.2.3"_ and open a PR titled the same
   - [ ] Await merge, then move on to step 2 described below

2. Checkout main and make sure it is up to date.

   ```shell
   git checkout main
   git fetch origin main
   git reset --hard origin/main
   ```

3. Update the version, make commits, and push a git tag with `tbump`.

   ```shell
   pip install tbump
   ```

   `tbump` will ask for confirmation before doing anything.

   ```shell
   # Example versions to set: 1.0.0, 1.0.0b1
   VERSION=
   tbump ${VERSION}
   ```

   Following this, the [CI system] will build and publish a release.

4. Reset the version back to dev, e.g. `1.0.1.dev` after releasing `1.0.0`.

   ```shell
   # Example version to set: 1.0.1.dev
   NEXT_VERSION=
   tbump --no-tag ${NEXT_VERSION}.dev
   ```

[github-activity]: https://github.com/executablebooks/github-activity
[pypi]: https://pypi.org/project/pytest-jupyterhub/
[ci system]: https://github.com/jupyterhub/pytest-jupyterhub/actions/workflows/release.yaml
