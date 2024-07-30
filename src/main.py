"""Python template app."""

from verboselogs import VerboseLogger

from src.helpers import init_logger


def main() -> None:
    """Program's entrypoint."""
    logger: VerboseLogger = init_logger(
        name="python-template", verbosity_level=3
    )
    logger.info("info")
    logger.error("error")
    logger.debug("debug")


if __name__ == "__main__":
    main()
