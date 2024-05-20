import unittest

from {{cookiecutter.project_slug}}.info_control import InfoControl


class MyTestCase(unittest.TestCase):
    def test_version(self):
        info_control = InfoControl()
        self.assertTrue(isinstance(info_control._load_version(), str))  # add assertion here


if __name__ == "__main__":
    unittest.main()
