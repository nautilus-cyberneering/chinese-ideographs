import os

from change_colour_profile.change_colour_profile import change_colour_profile


def main():
    source_images_path = os.environ["INPUT_SOURCE_IMAGES"].split(',')
    resized_images_path = os.environ["INPUT_DESTINATION_IMAGES"].split(',')
    profile = os.environ["INPUT_PROFILE"]
    for index, image_path in enumerate(source_images_path):
        print("Changing colour profile of ", image_path, "to", profile)
        change_colour_profile(image_path, resized_images_path[index], profile)


if __name__ == "__main__":
    main()
