import os

from validation.validate_size import validate_image_size


def main():
    source_images_path = os.environ["INPUT_SOURCE_IMAGES"].split(',')
    min_size = int(os.environ["INPUT_MIN_SIZE"])
    max_size = int(os.environ["INPUT_MAX_SIZE"])
    for image_path in source_images_path:
        print("Validating size of", image_path)
        validate_image_size(image_path, min_size, max_size)


if __name__ == "__main__":
    main()
