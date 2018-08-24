from logging import getLogger
from zipfile import ZipFile

from xml_zipper.generator.document import document

from concurrent.futures import ProcessPoolExecutor, wait

ZIP_COUNT = 50
XML_COUNT = 100


def bunch_zip(dirpath: str) -> None:
    getLogger(__name__).info(
        "generate %s zip files in the directory %s", ZIP_COUNT, dirpath
    )
    futures = []
    for i in range(ZIP_COUNT):
        with ProcessPoolExecutor() as executor:
            start = i * XML_COUNT + 1
            stop = start + XML_COUNT - 1
            single_zip(dirpath, start, stop)
            executor.submit(single_zip, dirpath, start, stop)
    wait(futures)


def single_zip(dirpath: str, start: int, stop: int) -> None:
    zip_name = f"{dirpath}/{start}_{stop}.zip"
    getLogger(__name__).info("generate file %s", zip_name)
    with ZipFile(zip_name, "w") as zip_with_xml:
        for i in range(start, stop + 1):
            zip_with_xml.writestr(f"{i}.xml", document())
