#!/usr/bin/env bash

# after cookiecutter generates the project from the template, this script is
# ran to perform any customization, cleanup, what ever...

# remove pycharm IDE info, if any (there shouldn't be, but we will be generating
# the virtual environment later and would prefer to avoid any potential issues)
rm -rf .idea
# clean out any old metrics (again, should be any unless they got checked into
# the cookiecutter template).
rm -f metrics/*
# again, shouldn't be anything in the cache, but just in case...
rm -rf tests/__pycache__

# symbolically link the front end taskfiles to match the build backend.
rm -f taskfiles/front-end.yaml taskfiles/front-end-vars.yaml
ln -s {{ cookiecutter.build_backend }}.yaml taskfiles/front-end.yaml
ln -s {{ cookiecutter.build_backend }}-vars.yaml taskfiles/front-end-vars.yaml

# return success
exit 0
