This is a [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating a Command Line Interface (CLI) python application framework 
that uses [loguru](https://loguru.readthedocs.io) for logging.  

[Poetry](https://python-poetry.org/) and [task](https://taskfile.dev/) are used for project management.

Please look at the `{{cookiecutter.project_slug}}/README.md` for framework details.

To create a new application using this template:

* [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

* Run:  cookiecutter https://github.com/royw/cookiecutter-clibones

After creating your new application skeleton, cd to the new project's directory then run:

* git init .      # optional
* task init       # initialized poetry environment
* task build      # verify the framework builds cleanly
* task main       # optional run the example application
* less README.md  # optional read the instructions ;-)

Start modifying the `src/__main__.py` and add your application code...

Enjoy!
