import os
import pathlib
import sys

from validation.filename import Filename
from validation.file_locator import file_locator


class InvalidImageFolderException(Exception):
    """Raised when the file is located in a wrong path"""
    pass


def validate_filepath(filepath):
    # Gold Image: data/000001/32/000001-32.600.2.tif
    # Base Image: data/000001/42/000001-32.600.2.tif

    actual_folder = os.path.dirname(filepath)

    filename = Filename(os.path.basename(filepath))

    expected_folder = file_locator(filename)

    if (expected_folder != actual_folder):
        raise InvalidImageFolderException(
            f'Invalid folder for image. The file "{ filepath }" should be in the folder "{ expected_folder }"')


def validate_filepaths(filepaths):
    for filepath in filepaths:
        validate_filepath(filepath)
