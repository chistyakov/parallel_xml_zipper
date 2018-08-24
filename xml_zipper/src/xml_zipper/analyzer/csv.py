import os
from logging import getLogger
from typing import List, Iterable, Tuple, TextIO

from xml_zipper.analyzer.document import Meta
from xml_zipper.analyzer.unzip import bunch_unzip


def save_meta(dirpath: str) -> None:
    levels_filename = os.path.join(dirpath, os.environ["LEVELS_FILENAME"])
    names_filename = os.path.join(dirpath, os.environ["NAMES_FILENAME"])
    with open(levels_filename, "w") as levels_f, open(names_filename, "w") as names_f:
        for meta_list in bunch_unzip(dirpath):
            flush(meta_list, levels_f, names_f)


def flush(meta_list: List[Meta], levels_file: TextIO, names_file: TextIO) -> None:
    getLogger(__name__).info("flush data")
    for level_by_id, names_by_id in as_rows(meta_list):
        levels_file.write(f"{level_by_id}\n")
        names_file.write(f"{names_by_id}\n")


def as_rows(meta_list: List[Meta]) -> Iterable[Tuple[str, str]]:
    level_by_id = "\n".join(f"{meta.id_},{meta.level}" for meta in meta_list)
    names_by_id = "\n".join(
        f"{meta.id_},{name}" for meta in meta_list for name in meta.names
    )
    yield level_by_id, names_by_id
