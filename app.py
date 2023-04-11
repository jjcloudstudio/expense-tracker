#this runs on ubuntu or wsl

# Import the required libraries
from wand.image import Image
from PIL import Image as PI
import pytesseract
import io
import sys, os

# Set the tesseract command

# Find all documents with .pdf extension in current directory
pdf_files = []

dir_path = os.getcwd()
for file in os.listdir(dir_path):
    if file.endswith(".pdf"):
        pdf_files.append(file)

# Setup a list and a dictionary which will be used to hold our images and 
# final_text. final_text will be organized by a key referring to the document
# name and page number.
req_image = []
final_text = {}

for pdf_file in pdf_files:
    # Open the PDF file using wand and convert it to jpeg
    image_pdf = Image(filename=pdf_file, resolution=300)
    image_jpeg = image_pdf.convert('pdf')

    # wand has converted all the separate pages in the PDF into separate image
    # blobs. We can loop over them and append them as a blob into the req_image
    # list.
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    # Now we just need to run OCR over the image blobs and store all of the 
    # recognized text in final_text.
    i = 1
    for img in req_image:
        txt = pytesseract.image_to_string(
            PI.open(io.BytesIO(img))
        )
        final_text[pdf_file + ' Page ' + str(i)] = txt
        i += 1

# Print the document name with page number and the text found by OCR.
for key, value in final_text.items():
    print("\nDocument: {}".format(key))
    print("\nThe final text is: \n")
    print(value)
