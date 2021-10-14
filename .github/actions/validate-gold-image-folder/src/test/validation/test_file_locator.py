import pytest

from validation.filename import Filename
from validation.file_locator import file_locator


def test_gold_image_localization():
    gold_image_filename = Filename('000001-32.600.2.tif')

    folder = file_locator(gold_image_filename)

    assert folder == 'data/000001/32'


def test_base_image_localization():
    gold_image_filename = Filename('000001-42.600.2.tif')

    folder = file_locator(gold_image_filename)

    assert folder == 'data/000001/42'
