from unittest import mock

import xml_zipper.generator as g


@mock.patch("xml_zipper.generator.generate_objects_count")
@mock.patch("xml_zipper.generator.generate_name", return_value="foo")
@mock.patch("xml_zipper.generator.generate_level", return_value="1")
@mock.patch(
    "xml_zipper.generator.generate_id",
    return_value="bd2ca695-346d-467e-a061-51eb405f4954",
)
def test_generate_xml_with_1_objects(mock_id, mock_level, mock_name, mock_count):
    xml_ = g.generate_xml()
    assert xml_ == (
        "<root>"
        '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954" />'
        '<var name="level" value="1" />'
        "<objects>"
        '<object name="foo" />'
        "</objects>"
        "</root>"
    )


@mock.patch("xml_zipper.generator.generate_objects_count", return_value=3)
@mock.patch("xml_zipper.generator.generate_name")
@mock.patch("xml_zipper.generator.generate_level", return_value="1")
@mock.patch(
    "xml_zipper.generator.generate_id",
    return_value="bd2ca695-346d-467e-a061-51eb405f4954",
)
def test_generate_xml_with_3_objects(mock_id, mock_level, mock_name, mock_count):
    mock_name.side_effect = ["foo", "bar", "baz"]
    xml_ = g.generate_xml()
    assert xml_ == (
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
