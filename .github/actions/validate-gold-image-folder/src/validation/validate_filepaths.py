import os
import pathlib
import sys


class FilepathException(Exception):
    """Raised when the file is located in a wrong path"""
    pass


def validate_filepath(filepath):
    pass


def validate_filepaths(filepaths):
    for filepath in filepaths:
        try:
            validate_filepath(filepath)
        except ValueError as error:
            raise FilepathException(f'Invalid file path {filepath}. {error}')
