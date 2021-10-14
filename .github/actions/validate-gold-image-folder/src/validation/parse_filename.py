import os
import pathlib
import sys


class FilepathException(Exception):
    """Raised when the file is located in a wrong path"""
    pass


def validate_filepath(filepath):
    # data/000001/32/000001-32.600.2.tif

    dirname = os.path.dirname(filepath)
    basename = os.path.basename(filepath)

    filename = Filename(basename)

    print(filename)


def parse_filename(filename):
    artwork_id, char, rest = filename.partition("-")
    purpose_code, char, rest = rest.partition(".")
    transformacion_code, char, rest = rest.partition(".")
    type_code, char, rest = rest.partition(".")
    extension, char, rest = rest.partition(".")
