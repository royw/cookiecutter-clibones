# cookiecutter-clibones

This is a [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating a Command Line Interface (CLI) python application framework 
that uses [loguru](https://loguru.readthedocs.io) for logging.  
 
A local development environment is included that uses:
 
* [Poetry](https://python-poetry.org/) Python packaging and dependency management.
* [Task](https://taskfile.dev/) is a task runner / build tool. 
* [MkDocs](https://www.mkdocs.org/) Project documentation with Markdown.
* [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) Material theme.
* [pytest](https://docs.pytest.org) unit testing.
* [pytest-cov](https://pytest-cov.readthedocs.io/) unit test coverage.
* [tox](https://tox.wiki) multiple python testing. 
* [radon](https://radon.readthedocs.io) code metrics.
* [Ruff](https://docs.astral.sh/ruff/) an extremely fast Python linter and code formatter, written in Rust.
* [FawltyDeps](https://github.com/tweag/FawltyDeps) FawltyDeps is a dependency checker for Python that finds 
  undeclared and/or unused 3rd-party dependencies in your Python project.

Several addition MkDocs plugins are used to proved automatic code reference in the
documentation.  No additional documentation configuration necessary.  Just run:

    task build
    task docs

Then open http://127.0.0.1:8000 with your browser.

## Prerequisites

* Install the task manager: [Task](https://taskfile.dev/)
* Install [Poetry](https://python-poetry.org/)
* Optionally install [pyenv-installer](https://github.com/pyenv/pyenv-installer)
  * Install dependent pythons, example:
  
    `pyenv local 3.11.9 3.12.3`

    *Note you may need to install some libraries for the pythons to compile cleanly.* 
    *For example on ubuntu (note I prefer `nala` over `apt`):*

  `sudo nala install tk-dev libbz2-dev libreadline-dev libsqlite3-dev lzma-dev python3-tk libreadline-dev`

Please look at the `{{cookiecutter.project_slug}}/README.md` for framework details.

## Installation

To create a new application using this template:

* [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

* Run:  cookiecutter https://github.com/royw/cookiecutter-clibones

After creating your new application skeleton, cd to the new project's directory then run:

* `git init .`     # optional
* `task build`      # verify the framework builds cleanly
* `task main`       # optional run the example application
* `less README.md`  # optional read the instructions ;-)

Start modifying the `src/*/__main__.py` and add your application code...

Enjoy!
