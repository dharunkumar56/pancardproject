import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\tesseract.exe'
from PIL import Image

def get_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)

    return text

# Specify the path to the image file
image_path = 'pan1-modified.jpg'

# Call the function to retrieve text from the image
result_text = get_text_from_image(image_path)

# Print the extracted text
print(result_text)
