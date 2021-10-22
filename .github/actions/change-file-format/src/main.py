import os
import json

from change_image_format.change_image_format import change_image_format


def process_input_json(input_json):
    # It gets a JSON object with information about the previous actions, and sets the input for this
    # action with the value of the output of the "resize" action
    # Input: {"added": [], "deleted": [], "modified": [], "renamed": [], "resize output": [...]}
    # Output: {..., "file format change output": [...]}

    # parse json
    data = json.loads(input_json)

    # parse path from all items
    data['file format change input'] = data['icc profile modify output'].copy()

    return data


def get_output_filename(input_filename, format):
    splittedFilename = os.path.splitext(input_filename)
    return splittedFilename[0]+"."+format


def main():

    def process_file(filename):
        output_filename = get_output_filename(filename)
        print("Converting ", filename, "to", format,
              "as", output_filename)
        change_image_format(filename, output_filename, format)
        processed_files.append(output_filename)

    processed_json = process_input_json(
        os.environ["INPUT_STATE"])
    format = os.environ["INPUT_FORMAT"]
    processed_files = []
    for image_path in processed_json['file format change input']:
        process_file(image_path)
    processed_json['file format change output'] = processed_files
    print("::set-output name=result::", json.dumps(processed_json))


if __name__ == "__main__":
    main()
