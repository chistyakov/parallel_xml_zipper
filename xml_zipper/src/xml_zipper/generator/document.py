import lxml.etree as et

import xml_zipper.generator.primitives as primitives


def document() -> str:
    root = et.Element("root")
    et.SubElement(root, "var", name="id", value=primitives.id_())
    et.SubElement(root, "var", name="level", value=primitives.level())
    root.append(objects())
    return et.tostring(root).decode()


def objects() -> et.Element:
    element = et.Element("objects")
    for _ in range(primitives.objects_count()):
        et.SubElement(element, "object", name=primitives.name())
    return element
