import os

from resizing.resize import resize_image


def parse_size_parametres():
    width = int(os.environ["INPUT_WIDTH"])
    height = int(os.environ["INPUT_HEIGHT"])
    return (width, height)


def main():
    source_images_path = os.environ["INPUT_SOURCE_IMAGES"].split(',')
    resized_images_path = os.environ["INPUT_DESTINATION_IMAGES"].split(',')
    output_size = parse_size_parametres()
    for index, image_path in enumerate(source_images_path):
        print("Resizing", image_path, "to", output_size[0],
             "x", output_size[1], "as", resized_images_path[index])
        resize_image(image_path, resized_images_path[index], output_size)


if __name__ == "__main__":
    main()
