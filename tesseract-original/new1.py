import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Perform OCR using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        return extracted_text.strip()

    except Exception as e:
        print("Error: ", e)
        return None

if __name__ == "__main__":
    image_path = "path/to/your/image.png"  # Replace with the actual path to your image
    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("No text could be extracted from the image.")
