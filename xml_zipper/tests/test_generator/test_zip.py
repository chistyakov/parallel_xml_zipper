from unittest import mock
from zipfile import ZipFile

import lxml.etree as et

import xml_zipper.generator.zip as g


def test_single_zip_creates_file(tmpdir):
    g.single_zip(dirpath=str(tmpdir), start=1, stop=100)
    assert ["1_100.zip"] == [fpath.basename for fpath in tmpdir.listdir()]


def test_single_zip_with_correct_number_of_xml(tmpdir):
    g.single_zip(dirpath=str(tmpdir), start=1, stop=100)
    zip_1_100_path = tmpdir.join("1_100.zip")
    with ZipFile(str(zip_1_100_path), "r") as z:
        assert 100 == len(z.namelist())


def test_single_zip_with_correct_xml(tmpdir):
    g.single_zip(dirpath=str(tmpdir), start=1, stop=100)
    zip_1_100_path = tmpdir.join("1_100.zip")
    with ZipFile(str(zip_1_100_path), "r") as z:
        with z.open("1.xml", "r") as xml_1_f:
            root = et.fromstring(xml_1_f.read())
            # there are more checks in tests for building of the document
            assert root.tag == "root"
            assert root[0].attrib["name"] == "id"
            assert root[1].attrib["name"] == "level"
            assert root[2].tag == "objects"


@mock.patch("xml_zipper.generator.zip.ZipFile.writestr")
def test_bunch_zip_creates_files(mock_writestr, tmpdir):
    g.bunch_zip(dirpath=str(tmpdir))
    zip_list = [fpath.basename for fpath in tmpdir.listdir()]
    assert "1_100.zip" in zip_list
    assert "4901_5000.zip" in zip_list
