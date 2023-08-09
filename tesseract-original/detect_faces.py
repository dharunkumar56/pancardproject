import cv2

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

# Path to the input image
image_path = 'test1.jpg'

# Detect faces in the image
num_faces = detect_faces(image_path)

# Print the number of faces detected
print(f"Number of faces detected: {num_faces}")
