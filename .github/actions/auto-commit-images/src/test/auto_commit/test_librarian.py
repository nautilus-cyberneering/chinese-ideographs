import pytest

from auto_commit.librarian import LibraryFilename, filter_media_library_files, filter_base_images


def test_base_image_type_check():
    filename = LibraryFilename("000002-42.600.2.tif")
    assert filename.is_base_image() == True


def test_media_library_files_filter():
    file_list = ["000002-42.600.2.tif", "not_media_library_file.txt"]

    only_library_files = filter_media_library_files(file_list)

    expected = ["000002-42.600.2.tif"]

    assert len(only_library_files) == len(expected)
    assert all([a == b for a, b in zip(only_library_files, expected)])


def test_media_library_base_image_files_filter():
    file_list = ["000002-42.600.2.tif",
                 "000002-32.600.2.tif"]  # Base and Gold images

    only_base_images = filter_base_images(file_list)

    expected = ["000002-42.600.2.tif"]

    assert len(only_base_images) == len(expected)
    assert all([a == b for a, b in zip(only_base_images, expected)])
