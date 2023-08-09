import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\tesseract.exe'

img = cv2.imread("sample.jpg")

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

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)

#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)

#     cropped = im2[y:y + h, x:x + w]

#     file = open("recognized.txt", "a")

#     text = pytesseract.image_to_string(cropped)

#     file.write(text)
#     file.write("\n")

#     file.close

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     coordinates.append([x, y, w, h])

# sorted_coordinates = sorted(coordinates, key=lambda item: item[0])

# for element in sorted_coordinates:
#     print(element[0], element[1], element[2], element[3])

# text_array = []

# for element in sorted_coordinates:
#     x, y, w, h = element

#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     cropped = im2[y:y + h, x:x + w]

#     file = open("recognized.txt", "a")

#     text = pytesseract.image_to_string(cropped)

#     file.write(text)

#     file.write("\n")

#     file.close

# def remove_special_characters(line):
#     return re.sub(r'\W+', '', line)

# filename = "recognized.txt"

# lines = []
# with open(filename, "r") as file:
#     for line in file:
#         line = line.rstrip("\n")  # Remove newline character
#         line = remove_special_characters(line)  # Remove special characters
#         if line:  # Check if line is not empty
#             lines.append(line)

# print("The recognized text is: ")

# for line in lines:
#     print(line)

# print()
# print("The remaining part:")

# result = []

# for i in range(len(lines)):
#     if(("name" in lines[i].lower()) and ("father" not in lines[i].lower()) and (i + 1 < len(lines))):
#         result.append(str(i) + " -> " + "Name: " + lines[i + 1])

#     if(("father" in lines[i].lower()) and (i + 1 < len(lines))):
#         result.append(str(i) + " -> " + "Father's Name: " + lines[i + 1])
    
#     if((("date" in lines[i].lower()) or ("birth" in lines[i].lower()) or ("dateofbirth" in lines[i].lower())) and (i + 1 < len(lines))):
#         result.append(str(i) + " -> " + "Date of birth: " + lines[i + 1])

#     if((("permanent" in lines[i].lower()) or ("account" in lines[i].lower()) or ("number" in lines[i].lower())) and (i + 1 < len(lines))):
#         result.append(str(i) + " -> " + "Account number: " + lines[i + 1])

# result = result[:-2]

# for info in result:
#     print(info)
#     print()



