import os
import json

from change_colour_profile.change_colour_profile import change_colour_profile


def parse_dvc_diff_ouput(dvc_diff):
    # It gets a plain string list with the added or modified files from the diff json.
    # Input: {"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}
    # Ouput: ['data/000001/32/000001-32.600.2.tif']
    # Code Review: parse_dvd_diff_ouput function should be moved to an independant action or dvc-diff action.

    # parse json
    data = json.loads(dvc_diff)

    # only interesting in added or modified files
    filenames = data['added'] + data['modified']

    # parse path from all items
    filenames = [path_object['path'] for path_object in filenames]

    return filenames


def main():
    source_images_path = parse_dvc_diff_ouput(
        os.environ["INPUT_SOURCE_IMAGES"])
    resized_images_path = os.environ["INPUT_DESTINATION_IMAGES"].split(',')
    profile = os.environ["INPUT_PROFILE"]
    for index, image_path in enumerate(source_images_path):
        print("Changing colour profile of ", image_path, "to", profile)
        change_colour_profile(image_path, resized_images_path[index], profile)


if __name__ == "__main__":
    main()
