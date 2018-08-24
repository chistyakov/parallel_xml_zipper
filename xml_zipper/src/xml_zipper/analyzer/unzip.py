from concurrent.futures import ProcessPoolExecutor, as_completed
from glob import glob
from logging import getLogger
from typing import Iterable, List
from zipfile import ZipFile

from xml_zipper.analyzer.document import extract_meta, Meta


def bunch_unzip(dirpath: str) -> Iterable[List[Meta]]:
    getLogger(__name__).info("read zip files from the directory %s", dirpath)
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(single_unzip, filepath)
            for filepath in glob(f"{dirpath}/*.zip")
        ]
        for fut in as_completed(futures):
            yield fut.result()


def single_unzip(filepath: str) -> List[Meta]:
    with ZipFile(filepath, "r") as zip_with_xml:
        getLogger(__name__).info("unzipped %s", filepath)
        meta_list = []
        for doc in zip_with_xml.infolist():
            getLogger(__name__).info("open %s", doc.filename)
            with zip_with_xml.open(doc, "r") as f:
                meta = extract_meta(f.read())
                meta_list.append(meta)
        return meta_list
