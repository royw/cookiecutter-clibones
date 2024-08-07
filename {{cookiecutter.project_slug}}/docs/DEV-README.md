<!--
SPDX-FileCopyrightText: 2024 Roy Wright

SPDX-License-Identifier: MIT
-->

# Welcome to this project's development environment!

What I'll attempt to do is explain the tool choices, their configuration, and
their interactions. Please note that development environments are a snapshot of
what is working, hopefully best working, as of now. Undoubtedly better tools,
different processes, and just personal preferences will change. So the best I
can hope for is preparing you for the start of this voyage! ;-)

<!-- TOC -->

- [Welcome to this project's development environment!](#welcome-to-this-projects-development-environment)
  - [Background](#background)
    - [In the beginning](#in-the-beginning)
    - [Today](#today)
  - [Development Environment Requirements](#development-environment-requirements)
  - [20,000 meter view](#20000-meter-view)
    - [Task](#task)
    - [Taskfile\*.yml](#taskfileyml)
  - [Under the hood](#under-the-hood) _ [Top level tables](#top-level-tables) _
  [check_pyproject](#check_pyproject) _
  [virtual environments](#virtual-environments) _ [src/ layout](#src-layout) _
  [testing](#testing) _ [tox](#tox) _ [matrix testing](#matrix-testing) _
  [coverage](#coverage) _ [mkdocs](#mkdocs) _ [pre-commit](#pre-commit) _
  [poetry.lock](#poetrylock) _ [reuse](#reuse) \* [git](#git)
  <!-- TOC -->

## Background

When the muse strikes, and it's time to create a new CLI application, I don't
want to spend time setting up the development environment. I just want to jump
into the new project. The current incarnation of my quick start, is a
cookiecutter template, cookiecutter-clibones. Since it had been a few years,
clibones is mostly new, with an updated ApplicationSettings base class (more
later).

### In the beginning

There was a confusing mess loosely referred to as python packaging. If curious,
a couple of excellent articles by Chris Warrick are:

- [How to improve Python packaging, or why fourteen tools are at least twelve too many](https://chriswarrick.com/blog/2023/01/15/how-to-improve-python-packaging/)
- [Python Packaging, One Year Later: A Look Back at 2023 in Python Packaging](https://chriswarrick.com/blog/2024/01/15/python-packaging-one-year-later/)

### Today

Things are a lot better. Still fractured. Still messy. But some experimenting
going on, which is good.

_"Hope springs eternal in the human breast: Man never is, but always to be
blest."_ - Alexander Pope _"An Essay on Man"_

Metadata is consolidating into a single
[pyproject.toml](https://pypi.python.org/pypi/pyproject.toml) file. Tool
configurations are also migrating to `pyproject.toml`. For the current state of
packaging, see [Python Packaging User Guide](https://packaging.python.org/) from
the [Python Packaging Authority](https://www.pypa.io) (PyPA).

Poetry is probably the leading package manager for the past few years. Alas,
times change. PyPA has filled out the Project definition in `pyproject.toml`.
Multiple build backends are easily supported. Newer package managers are out,
like [hatch](https://hatch.pypa.io/),
[pdm](https://packaging.python.org/en/latest/key_projects/#pdm),
[flit](https://packaging.python.org/en/latest/key_projects/#flit). Even
[Setuptools](https://setuptools.pypa.io/) is staying in the race.

So I decided this development environment will support both Poetry and Hatch.

Poetry is opinionated, uses non-standard revision syntax, and is a little dated
on its `pyproject.toml` usage (most settings - at least until poetry version 2
is released, are in `tool.poetry` table).

Hatch is hard core standards based, even if they have to wait for the standard
to be adopted. Should be interesting...

One more detail, I'm very much old school. The proper way to build a project is:

    config
    make
    make test
    make install

Nice and simple. Definitely not python package manager style. Luckily there are
tools available to help convert package manager commands into something simpler,
more elegant. I'm currently settled on [Task](https://taskfile.dev/).

Ok, final detail, I have spent years hating Sphinx. If you don't understand why,
then you've been lucky enough not to have to use sphinx. The great news is
[MkDocs](https://www.mkdocs.org/), a markdown base documentation tool, works
fantastic!

## Development Environment Requirements

Support:

- [Task](https://taskfile.dev/)
- [Poetry](https://python-poetry.org/)
- [Hatch](https://hatch.pypa.io/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [MkDocs](https://www.mkdocs.org/)
- [pytest](https://docs.pytest.org)
- [git](https://git-scm.com/)
  - [pre-commit](https://pre-commit.com/)
- [pyenv-installer](https://github.com/pyenv/pyenv-installer)
- testing multiple versions of python
  - [tox](https://tox.wiki) for poetry,
  - hatch matrices
- [radon](https://radon.readthedocs.io) code metrics
- [Ruff](https://docs.astral.sh/ruff/) code formatting
- Both [Ruff](https://docs.astral.sh/ruff/) and
  [MyPy](https://www.mypy-lang.org/) linters

## 20,000 meter view

### Task

Let's start with just running task:

    ➤ task
    task: [default] task --list
    task: Available tasks for this project:
    * build:                  Build the project.
    * build-docs:             Build the documentation.
    * check-licenses:         Check that all dependency licenses are acceptable for this project.
    * check-pyproject:        Check the consistency between poetry and hatch in the pyproject.toml file.
    * clean:                  Remove virtual environments and generated files.
    * coverage:               Run the unit tests with coverage.
    * docs:                   Create the project documentation and open in the browser.
    * format:                 Check and reformat the code to a coding standard.
    * init:                   initialize new project (only run once upon first creation of project).
    * lint:                   Perform static code analysis.
    * main:                   Run the __main__ module code, passing arguments to the module.  Example: task main -- --version
    * metrics:                Analyze the code.
    * pre-commit:             Must pass before allowing version control commit.
    * reuse-disable:          Disable using SPDX reuse for enforcing copyright and license.
    * reuse-enable:           Enable using SPDX reuse for enforcing copyright and license.
    * reuse-lint:             Perform reuse checks if pyproject.toml: tools.taskfile.reuse is set to "enabled"
    * serve-docs:             Start the documentation server and open browser at localhost:8000.
    * switch-to-hatch:        Switch development to use hatch instead of poetry.
    * switch-to-poetry:       Switch development to use poetry instead of hatch.
    * switch-to-setuptools:   Switch development to use setuptools.
    * tests:                  Run the unit tests for the supported versions of python.
    * version:                Run the project, having it return its version.

Cool, so looking over the list I'd guess the first thing I ought to do after
creating the project using cookiecutter is to initialize it:

    ➤ task init

then let's just go for broke and:

    ➤ task build

Seriously, to start a new project:

1. cookiecutter https://github.com/royw/cookiecutter-clibones
2. cd {your-project-name}
3. task init
4. task build
5. optionally: task switch-to-hatch
6. ...

Now the build task is the main rinse and repeat task, i.e., build it, correct
errors, build it,...

But say I prefer hatch, it is easy to switch:

    ➤ task switch-to-hatch

or maybe setuptools:

    ➤ task switch-to-setuptools

and to switch back to poetry with:

    ➤ task switch-to-poetry

Note, the editing of the pyproject.toml file to support the switch tasks is in
`scripts/swap_build_system.py`.

So now the project is building clean, whoooop! Before proceeding, let's take a
look at what the build task does:

    ➤ task build --summary
    task: build

    Build the project

    Format the project, check for code quality, check for compliance,
    perform unit testing, build distributables, build documentation,
    and run the application to display its version.

    commands:
     - Task: show-env
     - Task: format
     - Task: lint
     - pre-commit run --all-files
     - hatch -e dev build
     - Task: update-venv
     - Task: check-licenses
     - Task: coverage
     - Task: metrics
     - Task: build-docs
     - Task: version

Let's remove the switch tasks discussed above and the tasks ran by build from
the available task list:

    * check-pyproject:        Check the consistency between poetry and hatch in the pyproject.toml file.
    * clean:                  Remove virtual environments and generated files.
    * coverage:               Run the unit tests with coverage.
    * docs:                   Create the project documentation and open in the browser.
    * main:                   Run the __main__ module code, passing arguments to the module.  Example: task main -- --version
    * pre-commit:             Must pass before allowing version control commit.
    * reuse-disable:          Disable using SPDX reuse for enforcing copyright and license.
    * reuse-enable:           Enable using SPDX reuse for enforcing copyright and license.
    * reuse-lint:             Perform reuse checks if pyproject.toml: tools.taskfile.reuse is set to "enabled"
    * serve-docs:             Start the documentation server and open browser at localhost:8000.
    * tests:                  Run the unit tests for the supported versions of python.

and look at pre-commit task which is invoked in .pre-commit-config.yaml when ran
by pre-commit in the build task.

    ➤ task pre-commit --summary
    task: pre-commit

    Must pass before allowing version control commit.

    commands:
     - Task: check-pyproject

Both the tests and coverage tasks run pytest for each of the supported python
versions. The difference is for the coverage task, coverage generating options
are passed to pytest while for the tests task, they are not.

    ➤ task coverage --summary
    task: coverage

    Run the unit tests with coverage.

    commands:
     - hatch run -- test:pytest --cov-report term-missing --cov-report json:metrics/coverage.json --cov=foobar tests

    ➤ task tests --summary
    task: tests

    Run the unit tests for the supported versions of python.

    commands:
     - hatch run -- test:test

Removing the tests, coverage, and pre-commit tasks from the available task list:

    * clean:                  Remove virtual environments and generated files.
    * docs:                   Create the project documentation and open in the browser.
    * main:                   Run the __main__ module code, passing arguments to the module.  Example: task main -- --version
    * reuse-disable:          Disable using SPDX reuse for enforcing copyright and license.
    * reuse-enable:           Enable using SPDX reuse for enforcing copyright and license.
    * reuse-lint:             Perform reuse checks if pyproject.toml: tools.taskfile.reuse is set to "enabled"
    * serve-docs:             Start the documentation server and open browser at localhost:8000.

The clean task is pretty self-evident. If you want a totally clean environment,
then running clean followed by a switch-to-\_ task or the build task will do the
job:

    ➤ task clean
    ➤ task switch-to-poetry

or

    ➤ task clean
    ➤ task build

Now take a look at the docs task:

    ➤ task docs --summary
    task: docs

    Create the project documentation and open in the browser.

    commands:
     - Task: build-docs
     - Task: serve-docs

Note that build-docs is included in the build task, so you might want to just
run `task serve-docs` and examine your documentation. Now if you were in a
documentation editing phase, then the `task docs` would both build and show the
built documentation.

Now we are down to

    * main:                   Run the __main__ module code, passing arguments to the module.  Example: task main -- --version
    * reuse-disable:          Disable using SPDX reuse for enforcing copyright and license.
    * reuse-enable:           Enable using SPDX reuse for enforcing copyright and license.
    * reuse-lint:             Perform reuse checks if pyproject.toml: tools.taskfile.reuse is set to "enabled"

The reuse tasks support using the SPDX reuse system. You may enable or disable
using the system. The `reuse-lint` task is usually called by the `lint` task and
just conditionally runs "reuse lint" if reuse is enabled in the pyproject.toml
file's `tool.taskfile` table.

And that leaves us with the main task, which is just a shortcut for running the
project in the project manager's virtual environment. Try it:

    ➤ task main -- --help

### Taskfile\*.yml

Last topic on task, there are three task files:

    ➤ ls -l taskfile*
    -rw-rw-r-- 1 royw royw 5895 Jul 11 13:14 Taskfile-hatch.yml
    -rw-rw-r-- 1 royw royw 5333 Jul 11 12:19 Taskfile-poetry.yml
    lrwxrwxrwx 1 royw royw   18 Jul 10 14:12 Taskfile.yml -> Taskfile-hatch.yml

If you compare `Taskfile-hatch.yml` and `Taskfile-poetry.yml` you will notice
they are pretty similar, just using the appropriate hatch or poetry commands.
The symbolically linked `Taskfile.yml` is set with the `switch-to-*` tasks.

## Under the hood

Let's start with the mother of all config files, `pyproject.toml`. Yes,
`pyproject.toml` is intended to eventually hold all the configurations for all
of a project's development tools (ex: pytest, pylint, ruff,...), not just the
package managers.

### Top level tables

For practical purposes, `pyproject.toml` has three top level tables:

- build-system
- project
- tool

The `build-system` specifies which build backend is in use by the project. This
table is controlled with the `switch-to-*` tasks.

The `project` contains the project metadata and dependencies that are used by
pretty much all tools except poetry which keeps the metadata in `tools.poetry`
(current plans are for poetry version 2 to switch to using the `project` table -
fingers crossed).

And the `tool` table contains everything else. The naming convention is
`tool.{name}` where name is the tool/utility name (ex: `tool.ruff` for the ruff
tool's configuration).

### check_pyproject

A lot of the `tool.poetry` is now duplicated in the current `project` table
(giving poetry due credit, when poetry was created, these fields were not
defined in the project table, and therefore poetry correctly used `tool.poetry`
table). As of today, we have to deal with the pain of duplicated data in
`pyproject.toml`.

Therefore, I created `check_pyproject` utility that checks that duplicated
fields in `project` and `tool.poetry` tables have equivalent values. Equivalent
is used intentionally here as, for example, `project` dependencies use PEP 508
specifiers while poetry has their own tilde notation, which `check_pyproject`
translates to PEP 508 for comparison purposes. There are a few leftover fields
that cannot be compared, for example license, and are emitted as a warning to
the user to manually verify.

`check_pyproject` doesn't try to fix any problems. Its main purpose is to catch
issues that may creep in. For example: say you are using poetry, and naturally
do a `poetry add --group dev foo`. `check_pyproject` will point out that
`project.optional-dependencies.dev` table does not have 'foo' while
`tool.poetry.group.dev.dependencies` has 'foo>=0.1.1<0.2.0', expecting you to
simply copy the dependency specifier and paste it into the correct project
table.

### virtual environments

Both poetry and hatch make use of virtual environments. To enable both poetry
and hatch to share the same virtual environment and to share the same virtual
environment with PyCharm, the project's .venv/ virtual environment is used.

For poetry, the `task switch-to-poetry` sets the virtualenvs.in-project config
to true.

    ➤ poetry config virtualenvs.in-project true

For hatch, the type and path are set in the default environment which the other
environments inherit from.

    [tool.hatch.envs.default]
    type = "virtual"
    path = ".venv"

Finally, for pycharm:

    Settings - Project - Python Interpreter - Virtual Environment - Existing - Location:  .venv

Note, if you `task clean`, which deletes the .venv/ directory, then you ought to
recreate the virtual environment before using pycharm. The easiest is to just do
a `task run true` but any `task run ...` or `task shell` will do.

### src/ layout

The file structure is:

    .
    .venv/                    # virtual environment shared by: hatch, poetry, & IDE
    .reuse/                   # generated reuse templates
    dist/                     # generated distribution files
    docs/                     # documentation source files
    LICENSES/                 # license files
    metrics/                  # generated metrics reports
    node_modules              # generated by pre-commit
    scripts/                  # project build scripts
    site/                     # generated documentation
    src/                      # project source files
    tests/                    # unit test files
    .coverage                 # generated coverage database file
    .gitignore                # files not to check in to git
    .pre-commit-config-yaml   # pre-commit config file
    .python-version           # generated by pyenv list of python versions
    DEV-README.md             # this file
    mkdocs.yml                # mkdocs documentation system config file
    poetry.lock               # poetry resolved dependency lock file
    README.md                 # Standard README file in markdown format
    reuse.spdx                # generated bill of materials
    Taskfile.yml              # link to active taskfile
    Taskfile-hatch.yml        # hatch based taskfile
    Taskfile-poetry.yml       # poetry based taskfile
    tox.ini                   # tox configuration file

### testing

Pytest is used for unit testing. The test cases are in the `tests/` directory.
Configuration is in `pyproject.toml:tool.pytest.ini_options` table instead of
the traditional `pytest.ini` file.

#### tox

When using poetry, multiple python testing is via tox, with `tox.ini` being the
configuration file.

#### matrix testing

When using hatch, pytest is ran on each version of python in the test matrix in
`pyproject.toml`:

    [[tool.hatch.envs.test.matrix]]
    python = ["3.11", "3.12"]

#### coverage

Code coverage is performed using the default python version to run pytest +
coverage.

### lint

I'm a big fan of letting the computer find my issues, yes I like linters. So
there are a few linters in the lint task, some of which overlap.

    ➤ task lint --summary
    task: lint

    Perform static code analysis.

    commands:
     - poetry run -- ruff check --config pyproject.toml --fix src tests
     - poetry run -- scripts/run-mypy-all-python-versions.sh
     - poetry run -- fawltydeps --detailed || true
     - poetry run -- reuse lint
     - poetry run -- pyupgrade --py311-plus
     - scripts/fail_on_regex_match.sh "PyBind|Numpy|Cmake|CCache|Github|PyTest"
     - git ls-files -z -- "*.sh" | xargs -0 poetry run -- shellcheck

Note the use of two scripts. `scripts/run-mypy-all-python-versions.sh` and
`scripts/fail_on_regex_match.sh`. Both replace or mimic pre-commit tasks.

#### run-mypy-all-python-versions.sh

The default mypy pre-commit task requires hard-coding the python version in the
`.pre-commit-config.yaml` file. So created
`scripts/run-mypy-all-python-versions.sh` script that runs mypy for each python
major.minor version in the .python-version file which is controlled by pyenv.

#### fail_on_refex_match.sh

This is a simple test that searches for some common capitalization mistakes. The
intent is to find these problems in the build task instead of in the pre-commit.

### mkdocs

The configuration file for `mkdocs` is `mkdocs.yml`. The source file is
`docs/index.md` which is just a symbolic link to the project's `README.md` file.
Also by default the project's API is documented in the **code reference**
section using the code's docstrings. The HTML output is written to `site/`
directory.

Note that `scripts/gen_ref_pages.py` supports automatic API generation and is
used in `mkdocs.yml`.

While the default documentation is simple, it should suffice for most simple
projects and is easily expandable for more complex projects.

### pre-commit

Pre-commit is one of those love/hate relationships. I like sanitizing changes
going into my repo. But really dislike commits being blocked. The solution is
for `task build` to run the pre-commit checks. So once you have a passing build,
it really ought to be committable.

The pre-commit checks are defined in `.pre-commit-config.yaml` which includes
running `task pre-commit`.

    ➤ task pre-commit --summary
    task: pre-commit

    Must pass before allowing version control commit.

    commands:
     - Task: check-pyproject
     - Task: tests

### poetry.lock

Poetry will resolve dependencies then write them into the `poetry.lock` file,
which probably should in your version control system. The purpose of the
lockfile is to ensure that exactly the same versions of all the dependencies are
installed each time.

Hatch currently does not have an equivalent feature. There is a plugin,
[hatch-pip-compile](https://juftin.com/hatch-pip-compile/) that manages project
dependencies and lockfiles. References
[Feature request: Lock file support for applications](https://github.com/pypa/hatch/issues/749#top)

### reuse

My verdict is still out on [REUSE](https://reuse.software/). I have been on
projects where legal wants all the licenses we are using. Not a fun exercise. So
REUSE aims to facilitate managing a project's licenses. The pain point is adding
a copyright/license header to every file. The sweet point is automated bill of
material reporting. Time will tell...

Until then, I made using reuse optional. I added a table and setting to the
pyproject.toml:

    ### local Taskfile.yml options (not Taskfile options)

    [tool.taskfile]
    # For reuse copyright/license checking set reuse to either "enabled" or "disabled"
    # You should not directly edit this setting.  Instead, use the tasks "task reuse-enable" and
    # "task reuse-disable" as they also update the .git/hooks/pre-commit to either skip or not
    # skip the reuse hook.
    reuse = "disabled"

and split running reuse lint from the `lint` task to a new `reuse-lint` task
dependent upon the above reuse setting. All controlled with the `reuse-enable`
and `reuse-disable` tasks

### git

Currently, this project assumes git is the vcs. There are minimal direct usages
of git, so should be easily ported to another vcs. Also have intentionally
assumed not using GitHub, so no GitHub actions.

## CLIBones

CLIBones is a command line interface (CLI) application skeleton (Bones). The
main intent is to provide argument and config file handling with hardly any
effort, so it encapsulates argparse, ConfigParser in a `Settings` context
manager. Note that `Settings` uses argparse, giving you the power to have really
nice arguments (sorry, couldn't resist). This makes your main function look
something like:

    def main(args: list[str] | None = None) -> int:
        """The command line applications main function."""
        exit_code: int = 0
        with Settings(args=args) as settings:
            # some info commands (--version, --longhelp) need to exit immediately
            # after completion.  The quick_exit flag indicates if this is the case.
            if settings.quick_exit:
                return 0

            # TODO: Here be dragons!  In other words, your app goes here.
            exit_code = MyApp.run(settings)

        return exit_code

Please look in the `__main__.py` for more details on adding argument options and
parsers. And to complete the earlier forward reference, `ApplicationSettings` is
the parent class to `Settings` and contains the argument parsing.

Feel free to rip clibones out and roll your own bones.
