import os
import pathlib
import sys

# We are not implementing multiple transformations yet.
# {ARTWORK_ID}-{PURPOSE_CODE}.{TRANSFORMATION_CODE}.{TYPE_CODE}.{EXTENSION}


class FilenameException(Exception):
    """Raised when the filename format is invalid"""
    pass


def validate_artwork_id(artwork_id):
    if artwork_id == '':
        raise ValueError(
            "Missing artwork id. Artwork id should be between 000000 and 099999")
    if len(artwork_id) != 6:
        raise ValueError(
            "Invalid artwork length. Artwork id should have 6 digits. For example: 099999")
    if int(artwork_id) < 0 or int(artwork_id) > 99999:
        raise ValueError(
            "Wrong artwork id. Artwork id should be between 000000 and 099999")


def validate_purpose_code(purpose_code):
    if purpose_code == '':
        raise ValueError(
            "Missing purpose code. Purpose code should be: 32 or 42")
    if int(purpose_code) not in [32, 42]:
        raise ValueError(
            "Wrong purpose code. Purpose code should be: 32 or 42")


def validate_transformacion_code(transformacion_code):
    if transformacion_code == '':
        raise ValueError(
            "Missing transformacion code. Transformacion code should be: 600")
    if int(transformacion_code) not in [600]:
        raise ValueError(
            "Wrong transformacion code. Transformacion code should be: 600")


def validate_type_code(type_code):
    if type_code == "":
        raise ValueError(
            "Missing type code. Type code should be: 2")
    if type_code != "2":
        raise ValueError(
            "Wrong type code. Type code should be: 2")


def validate_extension(extension):
    if extension == "":
        raise ValueError(
            "Missing extention. Extension should be: tif")
    if extension != "tif":
        raise ValueError(
            "Wrong extention. Extension should be: tif")


def validate_filename(filename):
    artwork_id, char, rest = filename.partition("-")
    purpose_code, char, rest = rest.partition(".")
    transformacion_code, char, rest = rest.partition(".")
    type_code, char, rest = rest.partition(".")
    extension, char, rest = rest.partition(".")

    validate_artwork_id(artwork_id)
    validate_purpose_code(purpose_code)
    validate_transformacion_code(transformacion_code)
    validate_type_code(type_code)
    validate_extension(extension)


def validate_filenames(filenames):
    for filename in filenames:
        try:
            validate_filename(filename)
        except ValueError as error:
            raise FilenameException(f'Invalid filename {filename}. {error}')
