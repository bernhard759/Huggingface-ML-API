import os

from pdf2image import convert_from_bytes, convert_from_path
from PIL import Image
from transformers import pipeline

pipe = pipeline(
    task="image-classification", model="microsoft/dit-base-finetuned-rvlcdip"
)


def classify_pdf(filename: str = "filename.pdf"):
    """
    The classify_pdf function takes a pdf file as input and returns the classification of the first page.
    """
    images = convert_from_path(
        "filename.pdf",
        dpi=500,
        single_file=True,
        jpegopt="optimized",
        output_file="image.jpg"
    )
    # Saving pages in jpeg format
    for page in images:
        page.save("image.jpg", "JPEG")
    print("Converted pdf")
    image = Image.open("image.jpg")
    # Perform the classification
    classification = pipe(image)
    # File system cleanup
    if os.path.exists("image.jpg"):
        os.remove("image.jpg")
    if os.path.exists("filename.pdf"):
        os.remove("filename.pdf")
    if os.path.exists("images/image.jpg.ppm"):
        os.remove("images/image.jpg.ppm")
    return classification


def classify_image(image: str = "images.jpg"):
    """
    The classify_image function takes an image file and returns a classification.
    """
    # Open image
    images = Image.open(image)
    # Perform classification
    classification = pipe(images)
    # File system cleanup
    if os.path.exists("images.jpg"):
        os.remove("images.jpg")
    if os.path.exists("images/image.jpg.ppm"):
        os.remove("images/image.jpg.ppm")
    return classification