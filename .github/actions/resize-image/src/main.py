import os

from resizing.resize import resize_image


def parse_size_parametres():
    width = int(os.environ["INPUT_WIDTH"])
    height = int(os.environ["INPUT_HEIGHT"])
    return (width, height)


def main():
    source_image_path = os.environ["INPUT_SOURCE_IMAGE"]
    resized_image_path = os.environ["INPUT_DESTINATION_IMAGE"]
    output_size = parse_size_parametres()

    resize_image(source_image_path, resized_image_path, output_size)

    output = f"Resized image {resized_image_path}"
    print(output)


if __name__ == "__main__":
    main()
