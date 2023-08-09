from flask import Flask, render_template, request
import cv2
import pytesseract
import re
import cv2
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\tesseract.exe'

def detect_faces(image_path):
    # Load the Haar cascade XML file for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Return the number of faces detected
    return len(faces)

def is_all_digits(str):
    for c in str:
        if not c.isdigit():
            return False
    return True

def no_of_digits(str):
    cnt = 0

    for c in str:
        if c.isdigit():
            cnt += 1
    
    return cnt


def removed_words(str):
    if ("permanent" in str.lower()) or ("account" in str.lower()) or ("number" in str.lower()):
        return True
    if ("income" in str.lower()):
        return True
    if ("govt" in str.lower()) or ("india" in str.lower()):
        return True
    
    return False


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file selected'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected'
    
    file_extension = file.filename.rsplit('.', 1)[1].lower()

    if file and allowed_file(file_extension):

        if file_extension == "jpg":
            file.save('uploads/file1.jpg')
        
        if file_extension == "jpeg":
            file.save('uploads/file1.jpeg')
        
        if file_extension == "pdf":
            file.save("uploads/file2.pdf")
            images = convert_from_path('uploads/file2.pdf',500,poppler_path=r'C:\Program Files\poppler-23.05.0\Library\bin')
            images[0].save('uploads/file1.jpg', "JPEG")

        if file_extension == "jpg":
            img = cv2.imread("uploads/file1.jpg")
        if file_extension == "jpeg":
            img = cv2.imread("uploads/file1.jpeg")
        if file_extension == "pdf":
            img = cv2.imread("uploads/file1.jpg")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))

        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

        contours, hiearchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        im2 = img.copy()

        file = open("recognized.txt", "w+")
        file.write("")
        file.close()

        coordinates = []

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            coordinates.append([x, y, w, h])

        sorted_coordinates = sorted(coordinates, key=lambda item: item[0])

        for element in sorted_coordinates:
            print(element[0], element[1], element[2], element[3])

        text_array = []

        for element in sorted_coordinates:
            x, y, w, h = element

            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cropped = im2[y:y + h, x:x + w]

            file = open("recognized.txt", "a")

            text = pytesseract.image_to_string(cropped)

            file.write(text)

            file.write("\n")

            file.close

        def remove_special_characters(line):
            return re.sub(r'\W+', '', line)

        filename = "recognized.txt"

        lines = []
        with open(filename, "r") as file:
            for line in file:
                line = line.rstrip("\n")  # Remove newline character
                line = remove_special_characters(line)  # Remove special characters
                if line:  # Check if line is not empty
                    lines.append(line)

        for line in lines:
            print(line)

        # result = {}

        # for i in range(len(lines)):
        #     if((("permanent" in lines[i].lower()) or ("account" in lines[i].lower()) or ("number" in lines[i].lower())) and i + 1 < len(lines)):
        #         result["account_number"] = lines[i + 1]
        #     if("incometaxdepartment" in lines[i].lower() and i + 1 < len(lines) and ("name" not in result)):
        #         result["name"] = lines[i + 1]
        #         if(i + 2 < len(lines)):
        #             result["father_name"] = lines[i + 2]
        #         if(i + 3 < len(lines)):
        #             result["dob"] = lines[i + 3]
        
        # number_of_persons = detect_faces("uploads/file1.jpg")

        # result["number_of_persons"] = number_of_persons
        
        # error_messages = []

        # if "account_number" not in result:
        #     error_messages.append("account number not found")
        # if "dob" not in result:
        #     error_messages.append("dob not found")
        # if "name" not in result:
        #     error_messages.append("name not found")
        # if "father_name" not in result:
        #     error_messages.append("father's name not found")
        # if "account_number" in result:
        #     if len(result["account_number"]) < 10:
        #         error_messages.append("account number only partially visible")
        # if "number_of_persons" in result:
        #     if(result["number_of_persons"] == 0):
        #         error_messages.append("No faces detected")
        
        # result["error_messages"] = error_messages

        # return result

        result = {}
        names = []
        for line in lines:
            #check date
            if is_all_digits(line):
                result["dob"] = line
            
            #check account number
            elif len(line) == 10 and no_of_digits(line) == 4:
                result["account_number"] = line
            
            #check signature
            elif "signature" in line.lower():
                result["signature"] = "found"
            
            elif (not removed_words(line)):
                names.append(line)

        result["names_found"] = names

        number_of_persons = detect_faces("uploads/file1.jpg")

        result["number_of_persons"] = number_of_persons

        #Error messages

        error_messages = []

        if "dob" not in result:
            error_messages.append("dob not found")
        if "account_number" not in result:
            error_messages.append("account number not found")
        if "signature" not in result:
            error_messages.append("signature not found")
        if len(result["names_found"]) == 0:
            error_messages.append("no names found")
        if number_of_persons > 1:
            error_messages.append("more than one face detected")

        result["error_messages"] = error_messages

        return result
    else:
        return 'Invalid file format'

def allowed_file(file_extension):
    if(file_extension not in ["jpg", "jpeg", "pdf"]):
        return False
    return True

if __name__ == '__main__':
    app.run()
