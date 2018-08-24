import os
from concurrent.futures import ProcessPoolExecutor, wait
from logging import getLogger
from zipfile import ZipFile

from xml_zipper.generator.document import document


def bunch_zip(dirpath: str) -> None:
    zip_count = int(os.environ["ZIP_COUNT"])
    getLogger(__name__).info(
        "generate %s zip files in the directory %s", zip_count, dirpath
    )
    futures = []
    for i in range(zip_count):
        with ProcessPoolExecutor() as executor:
            xml_count = int(os.environ["XML_COUNT"])
            start = i * xml_count + 1
            stop = start + xml_count - 1
            single_zip(dirpath, start, stop)
            executor.submit(single_zip, dirpath, start, stop)
    wait(futures)


def single_zip(dirpath: str, start: int, stop: int) -> None:
    zip_name = f"{dirpath}/{start}_{stop}.zip"
    getLogger(__name__).info("generate file %s", zip_name)
    with ZipFile(zip_name, "w") as zip_with_xml:
        for i in range(start, stop + 1):
            zip_with_xml.writestr(f"{i}.xml", document())
