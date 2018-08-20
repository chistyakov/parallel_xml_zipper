import random
import string
import xml.etree.ElementTree as et
from uuid import uuid4
from zipfile import ZipFile

ZIP_COUNT = 50
XML_COUNT = 100

MIN_LEVEL = 1
MAX_LEVEL = 100

MIN_OBJECTS_COUNT = 1
MAX_OBJECTS_COUNT = 10
OBJECT_NAME_LENGTH = 5


def generate(path: str) -> None:
    for i in range(ZIP_COUNT):
        start = i * XML_COUNT + 1
        stop = start + XML_COUNT - 1
        generate_zip(path, start, stop)


def generate_zip(dirpath: str, start: int, stop: int) -> None:
    with ZipFile(f"{dirpath}/{start}_{stop}.zip", "w") as zip_with_xml:
        for i in range(start, stop + 1):
            zip_with_xml.writestr(f"{i}.xml", generate_xml())


def generate_xml() -> str:
    root = et.Element("root")
    et.SubElement(root, "var", name="id", value=generate_id())
    et.SubElement(root, "var", name="level", value=generate_level())
    root.append(generate_objects_element())
    return et.tostring(root).decode()


def generate_id() -> str:
    return str(uuid4())


def generate_level() -> str:
    return str(random.randint(MIN_LEVEL, MAX_LEVEL))


def generate_objects_element() -> et.Element:
    objects = et.Element("objects")
    for _ in range(generate_objects_count()):
        et.SubElement(objects, "object", name=generate_name())
    return objects


def generate_objects_count() -> int:
    return random.randint(MIN_OBJECTS_COUNT, MAX_OBJECTS_COUNT)


def generate_name():
    return "".join(random.choices(string.ascii_letters, k=OBJECT_NAME_LENGTH))
