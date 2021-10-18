import os
import pathlib
import sys


def file_locator(filename):
    return f'data/{filename.artwork_id}/{filename.purpose_code}'
