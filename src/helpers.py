"""Helper functions."""

import coloredlogs
from verboselogs import VerboseLogger


def init_logger(
    name: str,
    verbosity_level: int,
    formatting: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> VerboseLogger:
    """Initialize the program's logger.

    Parameters
    ----------
    name : str
        The logger's name.
    verbosity_level : int
        Verbosity log level.
    formatting : str, optional
        The log format.

    Returns
    -------
    verboselogs.VerboseLogger
        The logger.

    """
    levels: list[str] = ["INFO", "VERBOSE", "DEBUG", "SPAM"]
    logger = VerboseLogger(name)

    coloredlogs.install(
        logger=logger,
        level=levels[max(min(verbosity_level, len(levels) - 1), 0)],
        fmt=formatting,
        isatty=True,
    )

    return logger
