import random
import string
import xml.etree.ElementTree as et
from uuid import uuid4

OBJECT_NAME_LENGTH = 5
MAX_OBJECTS_COUNT = 10


def generate_xml() -> str:
    root = et.Element("root")
    et.SubElement(root, "var", name="id", value=generate_id())
    et.SubElement(root, "var", name="level", value=generate_level())
    root.append(generate_objects_element())
    return et.tostring(root).decode()


def generate_id() -> str:
    return str(uuid4())


def generate_level() -> str:
    return str(1)


def generate_objects_element() -> et.Element:
    objects = et.Element("objects")
    for _ in range(generate_objects_count()):
        et.SubElement(objects, "object", name=generate_name())
    return objects


def generate_objects_count() -> int:
    return random.randint(1, MAX_OBJECTS_COUNT)


def generate_name():
    return "".join(random.choices(string.ascii_letters, k=OBJECT_NAME_LENGTH))
