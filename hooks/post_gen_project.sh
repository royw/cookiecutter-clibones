#!/usr/bin/env bash

rm -rf .idea
rm -f metrics/*
rm -rf tests/__pycache__

rm -f taskfiles/front-end.yaml taskfiles/front-end-vars.yaml
ln -s {{ cookiecutter.build_backend }}.yaml taskfiles/front-end.yaml
ln -s {{ cookiecutter.build_backend }}-vars.yaml taskfiles/front-end-vars.yaml
exit 0
