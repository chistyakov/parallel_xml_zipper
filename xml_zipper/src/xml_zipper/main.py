import argparse
import logging
from argparse import Namespace

from xml_zipper.generator import generate
from xml_zipper.analyzer import analyze


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(processName)s[%(process)d]:%(name)s:%(levelname)s %(message)s",
    )
    args = parse_arguments()
    if args.action == "analyze":
        analyze(dirpath=args.dirpath)
    if args.action == "generate":
        generate(dirpath=args.dirpath)


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Generate and analyze zip files with xml."
    )
    parser.add_argument(
        "action", help="action to perform", choices=["generate", "analyze"]
    )
    parser.add_argument("dirpath", help="directory to store generated zip files")
    return parser.parse_args()


if __name__ == "__main__":
    main()
