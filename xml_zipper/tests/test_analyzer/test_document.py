import lxml.etree as et
import pytest

from xml_zipper.analyzer.document import extract_meta, Meta


def test_extract_meta_with_1_object():
    meta = extract_meta(
        "<root>"
        '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954"/>'
        '<var name="level" value="1"/>'
        "<objects>"
        '<object name="foo"/>'
        "</objects>"
        "</root>"
    )
    assert meta == Meta(
        id_="bd2ca695-346d-467e-a061-51eb405f4954", level="1", names=("foo",)
    )


def test_extract_meta_with_3_objects():
    meta = extract_meta(
        "<root>"
        '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954"/>'
        '<var name="level" value="1"/>'
        "<objects>"
        '<object name="foo"/>'
        '<object name="bar"/>'
        '<object name="baz"/>'
        "</objects>"
        "</root>"
    )
    assert meta == Meta(
        id_="bd2ca695-346d-467e-a061-51eb405f4954",
        level="1",
        names=("foo", "bar", "baz"),
    )


@pytest.mark.parametrize(
    "doc,exception",
    [
        (
            "<root"  # missing '>'
            '<var name="id" value="bd2ca695-346d-467e-a061-51eb405f4954"/>'
            '<var name="level" value="1"/>'
            "<objects>"
            '<object name="foo"/>'
            '<object name="bar"/>'
            '<object name="baz"/>'
            "</objects>"
            "</root>",
            et.ParseError,
        ),
        (
            "<root>"
            '<var name="id"/>'  # missing value
            '<var name="level" value="1"/>'
            "<objects>"
            '<object name="foo"/>'
            '<object name="bar"/>'
            '<object name="baz"/>'
            "</objects>"
            "</root>",
            KeyError,
        ),
    ],
)
def test_extract_meta_from_invalid_document(doc, exception):
    with pytest.raises(exception):
        extract_meta(doc)
