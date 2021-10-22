import pyvips
import os


def create_output_folder(image_path):
    os.makedirs(os.path.dirname(image_path), exist_ok=True)


def change_image_file_format(input_image_path, output_image_path):
    create_output_folder(input_image_path)
    image = pyvips.Image.new_from_file(input_image_path, access='sequential')
    image.write_to_file(output_image_path, Q=95)
