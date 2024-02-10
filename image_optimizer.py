from PIL import Image

def optimize_image(input_file, output_file, quality):
    """Optimizes an image by reducing its quality/file size.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path to save the optimized image.
        quality (int): The desired JPEG quality (1-100, lower means more compression).
    """

    image = Image.open(input_file)
    image.save(output_file, format="JPEG", quality=quality)

# Example usage:
optimize_image("my_image.jpg", "optimized_image.jpg", quality=75)
