#!/usr/bin/env python3
from argparse import ArgumentParser


def init_argparse():
    parser = ArgumentParser(
        description="{{cookiecutter.description}}",
    )

    return parser


def main():
    parser = init_argparse()
    parser.parse_args()


if __name__ == "__main__":
    main()
