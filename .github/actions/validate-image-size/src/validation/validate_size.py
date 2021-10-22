import pyvips


def check_image_size_is_valid(image, min_size_limit, max_size_limit):
    width = image.width
    height = image.height
    if (width > max_size_limit or height > max_size_limit
            or width < min_size_limit or height < min_size_limit):
        raise ValueError(
            "Wrong artwork size. Size must be between " +
            str(min_size_limit)+" and "
            + str(max_size_limit)+" pixels each side")


def validate_image_size(source_image_path, min_size_limit, max_size_limit):
    image = pyvips.Image.new_from_file(source_image_path, access='sequential')
    return check_image_size_is_valid(image, min_size_limit, max_size_limit)
