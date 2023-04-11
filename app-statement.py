import os
import pytesseract
from wand.image import Image
from PIL import Image as PI

# Set up the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# List of PDF files (replace with your own PDF file paths)
pdf_files = [
    'path/to/your/first/cheatsheet.pdf',
    #'path/to/your/second/pdf_file.pdf',
    # ...
]

output_file = 'output.txt'

with open(output_file, 'w', encoding='utf-8') as out_f:
    for pdf_file in pdf_files:
        with Image(filename=cheatsheet.pdf, resolution=300) as img:
            img.compression_quality = 99
            img.save(filename='temp.jpg')
        
        pil_img = PI.open('temp.jpg')
        txt = pytesseract.image_to_string(pil_img)
        
        out_f.write(txt)
        out_f.write('\n\n=== Next PDF ===\n\n')

os.remove('temp.jpg')

print(f"OCR output saved to {output_file}")
