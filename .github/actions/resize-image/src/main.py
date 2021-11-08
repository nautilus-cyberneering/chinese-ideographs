import os
import os.path
import json
import sys

from resizing.resize import resize_image


def process_input_json(input_json):
    # It gets a JSON object with information about the files removed and added, and returns the same object
    # with a new property with a list of the files to be modified
    # Input: {"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}
    # Output: {"added": ..., ..., "resize input": ["data/000001/32/000001-32.600.2.tif"]}

    # parse json
    data = json.loads(input_json)

    # parse path from all items
    data['resize input'] = [path_object['path']
                            for path_object in data['added'] + data['modified']]

    return data


def parse_size_parametres():
    width = int(os.environ["INPUT_WIDTH"])
    height = int(os.environ["INPUT_HEIGHT"])
    return (width, height)


def get_output_filename(input_filename):
    splittedFilename = os.path.splitext(input_filename)
    return splittedFilename[0]+"-resized"+splittedFilename[1]


def main():

    def process_file(filename):
        output_filename = get_output_filename(filename)
        print("Resizing ", filename, "to", output_size[0],
              "x", output_size[1], "as", output_filename)
        resize_image(filename, output_filename, output_size)
        processed_files.append(output_filename)

    processed_json = process_input_json(
        os.environ["INPUT_JOB_STATE"])
    output_size = parse_size_parametres()
    processed_files = []
    for image_path in processed_json['resize input']:
        process_file(image_path)
    processed_json['resize output'] = processed_files
    print("::set-output name=result::", json.dumps(processed_json))


if __name__ == "__main__":
    main()
