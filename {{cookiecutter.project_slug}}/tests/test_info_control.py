""" default tests for info_control.py """
from {{cookiecutter.project_slug}}.info_control import InfoControl


def test_version():
    info_control = InfoControl(app_package="{{cookiecutter.project_slug}}")
    version: str = info_control._load_version()
    assert isinstance(version, str)
    assert len(version) > 0


def test_default_version():
    info_control = InfoControl(app_package=".")
    version: str = info_control._load_version()
    assert isinstance(version, str)
    assert len(version) > 0
    assert version == InfoControl.DEFAULT_VERSION


def test_longhelp():
    info_control = InfoControl(app_package="{{cookiecutter.project_slug}}")
    longhelp: str = info_control._load_longhelp()
    assert longhelp is not None
    assert isinstance(longhelp, str)
    assert len(longhelp) > 0
    assert not longhelp.startswith("Long Help not available.")


def test_default_longhelp():
    info_control = InfoControl(app_package=None)
    longhelp: str = info_control._load_longhelp()
    assert longhelp is not None
    assert isinstance(longhelp, str)
    assert len(longhelp) > 0
    assert longhelp.startswith("Long Help not available.")
