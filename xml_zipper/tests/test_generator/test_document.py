from unittest import mock

import xml_zipper.generator.document as g


@mock.patch("xml_zipper.generator.document.primitives.objects_count", return_value=1)
@mock.patch("xml_zipper.generator.document.primitives.name", return_value="foo")
@mock.patch("xml_zipper.generator.document.primitives.level", return_value="1")
@mock.patch(
    "xml_zipper.generator.document.primitives.id_",
    return_value="bd2ca695-346d-467e-a061-51eb405f4954",
)
def test_generate_doc_with_1_object(mock_id, mock_level, mock_name, mock_count):
    doc = g.document()
    assert doc == (
        "<root>"
        '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954" />'
        '<var name="level" value="1" />'
        "<objects>"
        '<object name="foo" />'
        "</objects>"
        "</root>"
    )


@mock.patch("xml_zipper.generator.document.primitives.objects_count", return_value=3)
@mock.patch("xml_zipper.generator.document.primitives.name", return_value="foo")
@mock.patch("xml_zipper.generator.document.primitives.level", return_value="1")
@mock.patch(
    "xml_zipper.generator.document.primitives.id_",
    return_value="bd2ca695-346d-467e-a061-51eb405f4954",
)
def test_generate_xml_with_3_objects(mock_id, mock_level, mock_name, mock_count):
    mock_name.side_effect = ["foo", "bar", "baz"]
    doc = g.document()
    assert doc == (
        "<root>"
        '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954" />'
        '<var name="level" value="1" />'
        "<objects>"
        '<object name="foo" />'
        '<object name="bar" />'
        '<object name="baz" />'
        "</objects>"
        "</root>"
    )
