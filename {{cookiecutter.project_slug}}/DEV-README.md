To setup your dev environment:

* Install pyenv-installer.  https://github.com/pyenv/pyenv-installer

* Install dependent pythons, example:
  
  `pyenv local 3.11.9 3.12.3`

  Note you may need to install some libraries for the pythons to
compile cleanly, for example on ubuntu (note I prefer `nala` over `apt`):

  `sudo nala install tk-dev libbz2-dev libreadline-dev libsqlite3-dev lzma-dev python3-tk libreadline-dev`

Run nix-shell (https://nixos.org/) which will use shell.nix to install shell dependencies
so, you do not pollute your development system.  Note if you have locale
issues, you may find this alias useful:

  `alias nix-sh='LC_ALL=C.utf8 LANG=C nix-shell'`

Run poetry install which will install project dependencies.
* `loguru`  improved logging.  https://loguru.readthedocs.io
* `pytest`  unit testing.  https://docs.pytest.org
* `black`   code formatter.  https://github.com/psf/black
* `pathvalidate`. https://pathvalidate.readthedocs.io
* `tox`     multiple python testing. https://tox.wiki
* `mypy`    code lint. https://mypy.readthedocs.io
* `radon`    code metrics.  https://radon.readthedocs.io

Run `task build` to build the project using `Taskfile.yml`.  ref: https://taskfile.dev/
