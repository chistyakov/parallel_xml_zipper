import argparse
import logging
from argparse import Namespace

from xml_zipper.generator import generate


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    args = parse_arguments()
    generate(dirpath=args.dirpath)


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Generate and analyze zip files with xml."
    )
    parser.add_argument("--dirpath", help="directory to store generated zip files")
    return parser.parse_args()


if __name__ == "__main__":
    main()
