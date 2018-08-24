from dataclasses import dataclass

import lxml.etree as et


@dataclass
class Meta:
    id_: str
    level: str
    names: tuple


def extract_meta(document: str) -> Meta:
    root = et.fromstring(document)
    id_ = root.find("./var[@name='id']").attrib["value"]
    level = root.find("./var[@name='level']").attrib["value"]
    names = tuple(obj.attrib["name"] for obj in root.findall("./objects/object"))
    return Meta(id_, level, names)
