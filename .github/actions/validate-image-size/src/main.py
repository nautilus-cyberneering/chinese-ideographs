import os
import json

from validation.validate_size import validate_image_size


def process_input_json(input_json):
    # It gets a JSON object with information about the files removed and added, and returns the same object
    # with a new property with a list of the files to be checked
    # Input: {"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}
    # Output: {"added": ..., ..., "file size validation input": ["data/000001/32/000001-32.600.2.tif"]}

    # parse json
    data = json.loads(input_json)

    # parse path from all items
    data['file size validation input'] = [path_object['path']
                                          for path_object in data['added'] + data['modified']]

    return data


def main():
    processed_json = process_input_json(
        os.environ["INPUT_DVC_DIFF"])
    min_size = int(os.environ["INPUT_MIN_SIZE"])
    max_size = int(os.environ["INPUT_MAX_SIZE"])
    for image_path in processed_json['file size validation input']:
        print("Validating size of", image_path)
        validate_image_size(image_path, min_size, max_size)


if __name__ == "__main__":
    main()
