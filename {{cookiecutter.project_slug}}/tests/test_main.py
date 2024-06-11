from pathlib import Path

import pytest

import {{cookiecutter.project_slug}}.__main__


def test_main_pyproject():
    assert {{cookiecutter.project_slug}}.__main__.main([str(Path(__file__).parent / "good_pyproject.toml")]) == 0


def test_main_version():
    assert {{cookiecutter.project_slug}}.__main__.main(["--version"]) == 0


def test_main_longhelp():
    assert {{cookiecutter.project_slug}}.__main__.main(["--longhelp"]) == 0


def test_main_help():
    # --help is handled from argparse
    with pytest.raises(SystemExit) as e:
        {{cookiecutter.project_slug}}.__main__.main(["--help"])
    assert e.type == SystemExit
    assert e.value.code == 0
