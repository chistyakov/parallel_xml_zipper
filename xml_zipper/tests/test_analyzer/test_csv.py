from zipfile import ZipFile

from xml_zipper.analyzer.csv import save_meta


def test_save_meta(tmpdir):
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

    save_meta(str(tmpdir))

    with open(str(tmpdir.join("levels.csv")), "r") as f:
        assert f.read() == (
            "bd2ca695-346d-467e-a061-51eb405f4954,1\n"
            "9a5c2564-dd43-472a-a75d-7c928ad7c4da,2\n"
        )
    with open(str(tmpdir.join("object_names.csv")), "r") as f:
        assert f.read() == (
            "bd2ca695-346d-467e-a061-51eb405f4954,foo\n"
            "9a5c2564-dd43-472a-a75d-7c928ad7c4da,bar\n"
            "9a5c2564-dd43-472a-a75d-7c928ad7c4da,baz\n"
        )
