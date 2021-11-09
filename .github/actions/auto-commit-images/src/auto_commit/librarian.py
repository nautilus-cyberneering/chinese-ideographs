import os

from enum import Enum


class PurposeCode(Enum):
    GOLD_INDEX = 30
    GOLD_METADATA = 31
    GOLD_IMAGE = 32
    BASE_INDEX = 40
    BASE_METADATA = 41
    BASE_IMAGE = 42


class LibraryFilename():
    def __init__(self, filename):
        self.filename = filename
        self.parse(filename)

    @staticmethod
    def validate(filename):
        try:
            LibraryFilename(filename)
            return True
        except:
            return False

    def parse(self, filename):
        self.artwork_id, char, rest = filename.partition("-")
        purpose_code, char, rest = rest.partition(".")
        self.purpose_code = PurposeCode(int(purpose_code))
        self.transformacion_code, char, rest = rest.partition(".")
        self.type_code, char, rest = rest.partition(".")
        self.extension, char, rest = rest.partition(".")

    def __str__(self):
        return self.filename

    def is_base_image(self):
        return self.purpose_code is PurposeCode.BASE_IMAGE


def filter_media_library_files(filepaths):
    images = list(filter(lambda filepath: LibraryFilename.validate(
        os.path.basename(filepath)), filepaths))
    return images


def filter_base_images(filepaths):
    base_images = list(filter(lambda filepath: LibraryFilename(
        os.path.basename(filepath)).is_base_image(), filepaths))
    return base_images
