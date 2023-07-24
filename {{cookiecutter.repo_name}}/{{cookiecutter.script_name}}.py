#!/usr/bin/env python3
import logging
import sys
from argparse import ArgumentParser


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


if __name__ == "__main__":
    main()
