import pytest

from validation.validate_filepaths import InvalidImageFolderException, validate_filepath


def test_valid_folder_for_gold_image():
    validate_filepath("data/000001/32/000001-32.600.2.tif")


def test_valid_folder_for_base_image():
    validate_filepath("data/000001/42/000001-42.600.2.tif")


def test_invalid_folder_for_gold_image():
    with pytest.raises(InvalidImageFolderException):
        validate_filepath("data/000001/42/000001-32.600.2.tif")


def test_invalid_folder_for_base_image():
    with pytest.raises(InvalidImageFolderException):
        validate_filepath("data/000001/32/000001-42.600.2.tif")
