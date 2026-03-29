from file_processor import FileProcessor
import pytest

def test_file_write_read(tmpdir):
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_empty_string(tmpdir):
    file = tmpdir.join("empty.txt")

    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)

    assert content == ""


def test_large_data(tmpdir):
    file = tmpdir.join("large.txt")
    large_text = "A" * 10_000_000

    FileProcessor.write_to_file(file, large_text)
    content = FileProcessor.read_from_file(file)

    assert content == large_text


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file("non_existent_file.txt")


def test_overwrite_file(tmpdir):
    file = tmpdir.join("overwrite.txt")

    FileProcessor.write_to_file(file, "First")
    FileProcessor.write_to_file(file, "Second")

    content = FileProcessor.read_from_file(file)
    assert content == "Second"