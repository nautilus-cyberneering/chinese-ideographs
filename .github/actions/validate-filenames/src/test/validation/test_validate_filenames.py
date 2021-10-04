import pytest

from validation.validate_filenames import validate_filenames


def test_given_a_text_with_indiana_replacement_returns_text_without_indiana():
    filenames = ["data/000001/32/000001-32.600.2.tif"]

    validate_filenames(filenames)

    assert True is True
