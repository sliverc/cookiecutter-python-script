#!/usr/bin/env python3
import logging
import sys
from argparse import ArgumentParser
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent


def init_argparse():
    parser = ArgumentParser(
        description="{{cookiecutter.description}}",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the log level (default: INFO)",
    )

    return parser


def configure_logging(log_level):
    # Initialize logging to standard output (console)
    logging.basicConfig(
        stream=sys.stdout,
        filemode="w",
        level=getattr(logging, log_level),
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main():
    parser = init_argparse()
    args = parser.parse_args()

    configure_logging(args.log_level)

    try:
        # add script logic here
        pass
    except Exception:
        logging.exception("A unhandled error occurred. Exiting.")
        sys.exit(1)


if __name__ == "__main__":
    main()
