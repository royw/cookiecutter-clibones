""" Simple script to build package's __init__.py file with __version__ from pyproject.toml
and __doc__ from the project's README.md file."""

import argparse
import tomllib
from pathlib import Path

module_docstring = """# This file is generated by the pre_build.py script.
# DO NOT MANUALLY EDIT THIS FILE!  Edit the ../README.md file instead.
# 
# The pre_build.py script populates this file with:
# 
# __version__  set to the application's version from the pyproject.toml file.
# __doc__      set to the contents of the project's README.md file.
"""


def get_version():
    """load project version from the poetry pyproject.toml file"""
    pyproject = tomllib.load(open("pyproject.toml", "rb"))
    return pyproject['tool']['poetry']['version']


def get_project_documentation():
    """load ../README.md into the module docstring"""
    with open("README.md", "r") as f:
        return f"\"\"\"\n{f.read()}\"\"\""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package_dir", required=True, type=Path)
    args = parser.parse_args()
    package_dir = args.package_dir
    if package_dir.is_dir():
        output_path = package_dir / "__init__.py"
        if output_path.exists():
            output_path.unlink()
        output_path.touch()
        output_path.chmod(0o777)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f'{module_docstring}\n')
            f.write(f"__version__ = '{get_version()}'\n")
            f.write(f"__doc__ = {get_project_documentation()}\n")


if __name__ == "__main__":
    main()
