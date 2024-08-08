import io
import os

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, PlainTextResponse
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
from utils import classify_image, classify_pdf

# App
app = FastAPI(
    title="Document Classifier API",
    description="""An API for classifying documents into different categories""",
)

# Home route
@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
    Document Classifier API
    An API classifying documents into different categories.
    """
    return note

# Doc classifier
@app.post("/document-classifier")
async def get_document(file: UploadFile = File(...)):
    """
    This endpoint takes a PDF file as input and then returns a JSON response with the classes the PDF file belongs to.
    """
    files = await file.read()
    # save the file
    filename = "filename.pdf"
    with open(filename, "wb+") as f:
        f.write(files)
    # open the file and return the file name
    try:
        data = classify_pdf("filename.pdf")
        return data
    except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
        return "Unable to parse document! Please upload a valid PDF file."


# Image classifier
@app.post("/classify-image")
async def get_image(file: UploadFile = File(...)):
    """
    This endpoint takes an image file as input and then returns a JSON response with the classes the image file belongs to.
    """
    contents = io.BytesIO(await file.read())
    file_bytes = np.asarray(bytearray(contents.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    cv2.imwrite("images.jpg", img)
    try:
        data = classify_image("images.jpg")
        return data
    except ValueError as e:
        e = "Error! Please upload a valid image type."
        return e