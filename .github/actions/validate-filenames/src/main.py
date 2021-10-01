import os

from validation.validate_filename import validate_filename


def main():
    filenames = os.environ["INPUT_FILENAMES"]

    validate_filename(filenames)


if __name__ == "__main__":
    main()
