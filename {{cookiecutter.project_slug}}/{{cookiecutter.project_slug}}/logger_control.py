import sys
from argparse import ArgumentParser
from typing import Any
from loguru import logger

from pathvalidate.argparse import validate_filepath_arg


class LoggerControl:
    """Add logger control arguments (--loglevel, --debug, --quiet, --logfile) to CLI application."""

    VALID_LOG_LEVELS = [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ]  # cannot select NOTSET

    _help = {
        "output_group": "",
        "loglevel": f'Set verbosity level to one of the following: {VALID_LOG_LEVELS} (default: "INFO").',
        "debug": 'Output all messages (debug, info, warning, error, & critical).  Overrides "--loglevel".',
        "quiet": 'Only output error and critical messages.  Overrides "--loglevel" and "--debug".',
        "logfile": 'File to log messages enabled by "--loglevel" to.',
    }

    def add_arguments(self, parser: ArgumentParser) -> None:
        """Use argparse commands to add arguments to the given parser."""

        output_group = parser.add_argument_group(
            title="Logging Options", description=self._help["output_group"]
        )

        output_group.add_argument(
            "--loglevel",
            dest="loglevel",
            default="INFO",
            choices=LoggerControl.VALID_LOG_LEVELS,
            help=self._help["loglevel"],
        )

        output_group.add_argument(
            "--debug", dest="debug", action="store_true", help=self._help["debug"]
        )

        output_group.add_argument(
            "--quiet", dest="quiet", action="store_true", help=self._help["quiet"]
        )

        output_group.add_argument(
            "--logfile",
            dest="logfile",
            action="store",
            type=validate_filepath_arg,
            help=self._help["logfile"],
        )

    @staticmethod
    def setup(settings) -> None:
        level = "INFO"
        error_messages = []

        logger.remove()

        # convert settings to dictionary, so we can test if argument was passed
        settings_dict: dict[str, Any] = vars(settings)

        # the order of the loglevel processing is important.
        # --quiet has the highest priority followed by --debug then --loglevel
        if "loglevel" in settings_dict:
            level = settings_dict["loglevel"]
            if level not in LoggerControl.VALID_LOG_LEVELS:
                error_messages.append(
                    f"Invalid log level {level}, "
                    f"should be one of the following: {LoggerControl.VALID_LOG_LEVELS}"
                )
                level = "INFO"

        if "debug" in settings_dict and settings_dict["debug"]:
            level = "DEBUG"

        if "quiet" in settings_dict and settings_dict["quiet"]:
            level = "ERROR"

        logger.add(sys.stdout, level=level)

        if "logfile" in settings_dict and settings_dict["logfile"]:
            filename = settings_dict["logfile"]
            try:
                logger.add(filename, level=level)
            except IOError as ex:
                error_messages += [f"Could not open logfile ({filename}): {ex}"]

        for msg in error_messages:
            logger.error(msg)
