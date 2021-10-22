import os
import json

from modify_icc_profile.modify_icc_profile import modify_icc_profile


def process_input_json(input_json):
    # It gets a JSON object with information about the previous actions, and sets the input for this
    # action with the value of the output of the "resize" action
    # Input: {"added": [], "deleted": [], "modified": [], "renamed": [], "resize output": [...]}
    # Output: {..., "icc profile modify input": [...]}
    # Code Review: parse_dvd_diff_ouput function should be moved to an independant action or dvc-diff action.

    # parse json
    data = json.loads(input_json)

    # parse path from all items
    data['icc profile modify input'] = data['resize output'].copy()

    return data


def get_output_filename(input_filename):
    splittedFilename = os.path.splitext(input_filename)
    return splittedFilename[0]+"-icc-profile-modified"+splittedFilename[1]


def main():

    def process_file(filename):
        output_filename = get_output_filename(filename)
        print("Modifying image ICC profile of ", filename, "to", profile,
              "as", output_filename)
        modify_icc_profile(filename, output_filename, profile)
        processed_files.append(output_filename)

    processed_json = process_input_json(
        os.environ["INPUT_STATE"])
    profile = os.environ["INPUT_PROFILE"]
    processed_files = []
    for image_path in processed_json['icc profile modify input']:
        process_file(image_path)
    processed_json['icc profile modify output'] = processed_files
    print("::set-output name=result::", json.dumps(processed_json))


if __name__ == "__main__":
    main()
