""" Simple script to build package's __init__.py file with {{cookiecutter.project_slug}}.version from
pyproject.toml and __doc__ from the project's README.md file."""

import argparse
from pathlib import Path
from loguru import logger


module_docstring = """# This file is generated by the bin/mk_module_init_py.py script.
# DO NOT MANUALLY EDIT THIS FILE!  
# Edit the ../README.md file instead for the module docstring
# and the pyproject.toml file for the project version,
# then run: mk_module_init_py.py --package_dir src/{{cookiecutter.project_slug}} 
# 
# The mk_module_init_py.py script populates this file with:
# 
# __doc__      set to the contents of the project's README.md file.
# version      set to the application's version from the pyproject.toml file.
"""

post_commands = """

from usingversion import getattr_with_version

__getattr__ = getattr_with_version("{{cookiecutter.project_slug}}", __file__, __name__)
"""


def get_project_documentation():
    """load ../README.md into the module docstring"""
    with open(Path.cwd() / "README.md", "r") as f:
        return f"\"\"\"\n{f.read()}\"\"\""


def generate_module_init_file(package_dir: Path) -> None:
    output_path = package_dir / "__init__.py"
    if output_path.exists():
        output_path.unlink()
    output_path.touch()
    output_path.chmod(0o777)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f'{module_docstring}\n')
        f.write(f"__doc__ = {get_project_documentation()}\n")
        f.write(f'{post_commands}\n')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package_dir", required=True, type=Path)
    args = parser.parse_args()
    if args.package_dir.is_dir():
        generate_module_init_file(args.package_dir)
    else:
        logger.error("package_dir must be a directory")


if __name__ == "__main__":
    main()
