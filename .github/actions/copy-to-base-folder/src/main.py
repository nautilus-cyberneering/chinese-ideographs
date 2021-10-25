import os
import json
import re
import shutil


def process_input_json(input_json):
    # It gets a JSON object with information about the previous actions, and sets the input for this
    # action with the value of the output of the "resize" action
    # Input: {"added": [], "deleted": [], "modified": [], "renamed": [], "resize output": [...]}
    # Output: {..., "file format change output": [...]}

    # parse json
    data = json.loads(input_json)

    # parse path from all items
    data['move to base folder input'] = data['file format change output'].copy()

    return data


def get_output_filename(input_filename):
    splittedFilename = os.path.split(input_filename)
    return re.sub(r'/32$', '/42/', splittedFilename[0]) + splittedFilename[1].replace('-32.', '-42.')


def create_output_folder(image_path):
    os.makedirs(os.path.dirname(image_path), exist_ok=True)


def main():

    def copy_file(filename):
        output_filename = get_output_filename(filename)
        print("Copying ", filename, "to", output_filename)
        create_output_folder(output_filename)
        shutil.copy(filename, output_filename)
        processed_files.append(output_filename)

    processed_json = process_input_json(
        os.environ["INPUT_STATE"])
    processed_files = []
    for image_path in processed_json['move to base folder input']:
        copy_file(image_path)


if __name__ == "__main__":
    main()