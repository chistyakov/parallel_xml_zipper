from zipfile import ZipFile

import xml_zipper.analyzer.unzip as a
from xml_zipper.analyzer.document import Meta


def test_single_unzip(tmpdir):
    zip_1_100_path = tmpdir.join("1_100.zip")
    with ZipFile(str(zip_1_100_path), "w") as z:
        z.writestr(
            "1.xml",
            (
                "<root>"
                '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954" />'
                '<var name="level" value="1" />'
                "<objects>"
                '<object name="foo" />'
                "</objects>"
                "</root>"
            ),
        )
        z.writestr(
            "2.xml",
            (
                "<root>"
                '<var name="id" value="9a5c2564-dd43-472a-a75d-7c928ad7c4da" />'
                '<var name="level" value="2" />'
                "<objects>"
                '<object name="bar" />'
                '<object name="baz" />'
                "</objects>"
                "</root>"
            ),
        )
    meta_list = a.single_unzip(str(zip_1_100_path))

    assert [
        Meta(id_="bd2ca695-346d-467e-a061-51eb405f4954", level="1", names=("foo",)),
        Meta(
            id_="9a5c2564-dd43-472a-a75d-7c928ad7c4da", level="2", names=("bar", "baz")
        ),
    ] == meta_list
