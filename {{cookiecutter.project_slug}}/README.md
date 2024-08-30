<!--
SPDX-FileCopyrightText: 2024 Roy Wright
SPDX-License-Identifier: MIT
-->

# {{cookiecutter.project_name}}

[![PyPI - Version](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg)](https://pypi.org/project/{{cookiecutter.project_slug}})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}.svg)](https://pypi.org/project/{{cookiecutter.project_slug}})

---

## Table of Contents

<!-- TOC -->
* [{{cookiecutter.project_name}}](#{{cookiecutter.project_name}})
  * [Table of Contents](#table-of-contents)
  * [Overview](#overview)
  * [Getting Started](#getting-started)
  * [Architecture](#architecture)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Workflows](#workflows)
    * [Tasks](#tasks)
    * [Switching between Poetry and Hatch](#switching-between-poetry-and-hatch)
    * [Adding a dependency using poetry](#adding-a-dependency-using-poetry)
    * [Adding a dependency using hatch](#adding-a-dependency-using-hatch)
  * [License](#license)
  * [References](#references)
    * [Build tools](#build-tools)
      * [FawltyDeps](#fawltydeps)
    * [Documentation tools](#documentation-tools)
<!-- TOC -->

## Overview

This application used
[cookiecutter-clibones](https://github.com/royw/cookiecutter-clibones), a CLI
application framework based on the argparse standard library with loguru
logging. [Poetry](https://python-poetry.org/) and
[taskfile](https://taskfile.dev/) are used for project management.

## Getting Started

After creating the project with:

    cookiecutter https://github.com/royw/cookiecutter-clibones

and answering the project questions, this framework was created. To use, you
need to run:

    task init
    task build

The framework is now ready for all of your good stuff.

A couple of useful commands:

    task --list-all     # shows available tasks
    less Taskfile.yml   # shows the commands that form each task.  Feel free to customize.
    poetry lock         # for when the poetry.lock gets out of sync with pyproject.toml

## Architecture

The architecture used is a Settings context manager that handles all the command
line and config file argument definition, parsing, and validation.

The application's entry point is in `{{cookiecutter.project_slug}}/__main__.py`.
In `__main.py__` there are several TODOs that you will need to visit and clear.

The application may be run with any of the following:

- `python3 -m {{cookiecutter.project_slug}} --help`
- `poetry run python3 -m {{cookiecutter.project_slug}} --help`
- `task main --help`

So in general, for each command line argument you ought to:

- optionally add an argument group to the parser in `Settings.add_arguments()`
- add argument to the parser in `Settings.add_arguments()`
- optionally add validation to `Settings.validate_arguments()`

Refer to `application_settings.py` which implements help and logging as
examples.

The `__example_application()` demonstrates using a `GracefulInterruptHandler` to
capture ^C for a main loop.

Next take a look at `main.main()` which demonstrates the use of the Settings
context manager.

The `Settings` does have a few extra features including:

- config files are supported for any command arguments you want to persist.
- standard logging setup via command line arguments.

## Development installation

### Development Prerequisites

- Install the task manager: [Task](https://taskfile.dev/)
- Optionally install [pyenv-installer](https://github.com/pyenv/pyenv-installer)

  - Install dependent pythons, example:

    `pyenv local 3.11.9 3.12.3`

  _Note you may need to install some libraries for the pythons to compile
  cleanly._ _For example on ubuntu (note I prefer `nala` over `apt`):_

  `sudo nala install tk-dev libbz2-dev libreadline-dev libsqlite3-dev lzma-dev python3-tk libreadline-dev`

- Recommended to upgrade pip to latest.
- Optionally install [Poetry](https://python-poetry.org/)
- Optionally install [Hatch](https://hatch.pypa.io/)
- Optionally install [setuptools](https://setuptools.pypa.io/)
  - Install [build](https://build.pypa.io/)

Install the package using your favorite dev tool. Examples:

- `git clone git@github.com:royw/{{cookiecutter.project_slug}}.git`
- `cd {{cookiecutter.project_slug}}`
- `task init`
- `task make`

_Note, `task init` will run `git init .`, `git add` the initial project files,
and do a `git commit`. If you are using another VCS, please first edit the init
task in the `Taskfile.yaml` file._

See the [Developer README](DEV-README.md) for detailed information on the
development environment.

## License

`{{cookiecutter.project_slug}}` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.

## References

- The [Python Packaging User Guide](https://packaging.python.org/en/latest)
- The
  [pyproject.toml specification](https://pypi.python.org/pypi/pyproject.toml)
- The [Poetry pyproject.toml metadata](https://python-poetry.org/docs/pyproject)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [Setuptools](https://setuptools.pypa.io/)
