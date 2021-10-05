import pyvips


def resize_image(source_image_path, resized_image_path, output_size):
    image = pyvips.Image.new_from_file(source_image_path, access='sequential')
    width = image.width
    height = image.height
    factor_width = output_size[0] / width
    factor_height = output_size[1] / height
    factor = min(factor_height, factor_width)
    result = image.resize(factor, kernel='lanczos2')
    result.write_to_file(resized_image_path)
    print("Image resized sucessfully")
