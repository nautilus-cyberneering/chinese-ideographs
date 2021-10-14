import pytest

from validation.filename import Filename


def test_instantiation_from_string():
    gold_image_filename = Filename('000001-32.600.2.tif')

    assert gold_image_filename.artwork_id == '000001'
    assert gold_image_filename.purpose_code == '32'
    assert gold_image_filename.transformacion_code == '600'
    assert gold_image_filename.type_code == '2'
    assert gold_image_filename.extension == 'tif'
