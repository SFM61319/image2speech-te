"""
OCR Module, provides functionality to scan and read text from images.
"""


import pytesseract


def read_text_from_image(image_path: str) -> str:
    """
    Reads text from an image using Tesseract OCR.

    Args:
        image_path: The path to the image file.

    Returns:
        A string containing the text in the image.
    """

    # Scan and retrieve text from the image.
    image = pytesseract.image_to_string(image_path, lang="te")

    # Return the text.
    return str(image)
