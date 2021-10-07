import pyvips
<<<<<<< HEAD
import os
=======
>>>>>>> 505beefe78bf0048981b0cfea41316e5eb2f1e62


def getImageFactor(image, output_size):
    width = image.width
    height = image.height
    factor_width = output_size[0] / width
    factor_height = output_size[1] / height
    return min(factor_height, factor_width)


<<<<<<< HEAD
def createOutputFolder(resized_image_path):
    os.mkdir(os.path.dirname(resized_image_path))


=======
>>>>>>> 505beefe78bf0048981b0cfea41316e5eb2f1e62
def resize_image(source_image_path, resized_image_path, output_size):
    image = pyvips.Image.new_from_file(source_image_path, access='sequential')
    result = image.resize(getImageFactor(
        image, output_size), kernel='lanczos2')
<<<<<<< HEAD
    createOutputFolder(resized_image_path)
    result.write_to_file(resized_image_path)
=======
    result.write_to_file(resized_image_path)
    print("Image", source_image_path, "resized to", result.width,
          "x", result.height, "as", resized_image_path)
>>>>>>> 505beefe78bf0048981b0cfea41316e5eb2f1e62
