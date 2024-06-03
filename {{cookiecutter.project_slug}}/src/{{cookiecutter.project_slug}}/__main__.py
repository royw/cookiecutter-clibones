"""
This is a sample Python CLI script.  Set up command line arguments in a class derived from ApplicationSettings.

You need to update the following class variables in Settings class to match your needs:

* project_name
* project_package
* project_description

and then add any arguments to Settings.add_arguments() and Settings.validate_arguments() methods.

Finally, add your application into the main() method.
"""

import argparse
import atexit
import pprint
import sys

from loguru import logger
from time import sleep
from typing import List, Sequence

from .application_settings import ApplicationSettings
from .graceful_interrupt_handler import GracefulInterruptHandler

# Some loguru formats to get you started, used in main()

# Default loguru format for colorized output
LOGURU_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "\
                "<level>{level: <8}</level> | "\
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
# removed the timestamp from the logs
LOGURU_MEDIUM_FORMAT = "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
# just the colorized message in the logs
LOGURU_SHORT_FORMAT = "<level>{message}</level>"

# TODO remove example application constants
DEFAULT_COUNT = 5
MAX_COUNT = 10
MIN_COUNT = 1


# noinspection PyMethodMayBeStatic
class Settings(ApplicationSettings):
    """Where the project's initial state (i.e. settings) are defined.

    Settings extends the generic ApplicationSettings class which parses the command line arguments.

    Usage::

        with Settings() as settings:
        try:
            app.execute(settings)
            exit(0)
        except ArgumentError as ex:
            error(str(ex))
            exit(1)
    """

    # TODO: verify the __project_* variables are correct

    __project_name: str = "{{cookiecutter.project_slug}}"
    """The name of the project"""

    __project_package: str = "{{cookiecutter.project_slug}}"
    """The name of the package this settings belongs to. """

    __project_description: str = (
        "{{cookiecutter.project_short_description}}"
    )
    """A short description of the application."""

    def __init__(self, args: Sequence[str] | None = None) -> None:
        """Initialize the base class."""

        super().__init__(
            app_name=Settings.__project_name,
            app_package=Settings.__project_package,
            app_description=Settings.__project_description,
            config_sections=[Settings.__project_name],
            args=args,
        )

    def add_parent_parsers(self) -> list[argparse.ArgumentParser]:
        """This is where you should add any parent parsers for the main parser.

        :return: a list of parent parsers
        """
        return []

    def add_arguments(self, parser: argparse.ArgumentParser, defaults: dict[str, str]) -> None:
        """This is where you should add arguments to the parser.

        To add application arguments, you should override this method.

        :param parser: the argument parser with --conf_file already added.
        :param defaults: the default dictionary usually loaded from a config file
        """
        # use normal argparse commands to add arguments to the given parser.  Example:

        # TODO: Remove example app --count N argument
        app_group = parser.add_argument_group("Application arguments")
        app_group.add_argument(
            "--count",
            type=int,
            default=DEFAULT_COUNT,
            help=f"How many times (0-{MAX_COUNT} to execute the example loop (default: {DEFAULT_COUNT})",
        )
        return

    def validate_arguments(self, settings: argparse.Namespace, remaining_argv: List[str]) -> list[str]:
        """This provides a hook for validating the settings after the parsing is completed.

        :param settings: the settings object returned by ArgumentParser.parse_args()
        :param remaining_argv: the remaining argv after the parsing is completed.
        :return: a list of error messages or an empty list
        """
        result = []
        # TODO: Remove example app validation: --count=N where: MIN_COUNT < N <= MAX_COUNT
        if settings.count > MAX_COUNT:
            result.append(f"--count ({settings.count}) > 10")
        if settings.count < MIN_COUNT:
            result.append(f"--count ({settings.count}) < {MIN_COUNT}")
        return result


# TODO: remove example application
def __example_application(settings: argparse.Namespace) -> None:
    """This is just an example application, replace with the real application.

    :param settings: the settings object returned by ArgumentParser.parse_args()
    """
    with GracefulInterruptHandler() as handler:
        logger.debug("Executing Example Application")
        logger.info(f"Settings: {pprint.pformat(vars(settings), indent=2)}")

        for iteration in range(0, settings.count):
            sleep(1)
            print(".", end="", flush=True)
            # to break out of loop when interrupt (^C) is pressed
            if handler.interrupted:
                logger.error(f"Loop Interrupted after {iteration} iterations")
                break
        print("\n")

        logger.debug("Example Application Complete")


def main():
    """The command line applications main function."""
    logger.remove(None)
    logger.add(sys.stderr, level="DEBUG", format=LOGURU_FORMAT)

    with Settings() as settings:
        # TODO: replace invoking the example application with your application's entry point
        __example_application(settings)


def cleanup():
    """Cleans up the application just before exiting."""
    # TODO: add any cleanup necessary.
    logger.debug("Cleaning up")


if __name__ == "__main__":
    atexit.register(cleanup)
    main()
