Problem statement:
An application that takes an pan card and verfies whether the document is correct or not. It gives a object containing the details in the pan card along with proper error messages

Interface:

A simple button in which user can select a file to be uploaded

The application runs as a api which gets the image in a post request and does the validating and sends an object containing the details along with the error messages

Technologies used:

Front-end: HTML, CSS
Backend: Flask(Python)
Text-recognition: tesseract (open-source)

Usage of tesseract:

It is a tool which is used to get text from an image.

Backend logic used:

After getting the image from the user
1. It is stored in uploads folder(in the name of file1.jpg)
2. Tesseract extracts text from the image and form something called contours, which are boxes around the text areas in the image
3. Each contour contains the top left coordinate of the rectangle containing the text and also the bottom right coordinate

Logic to find which box belongs to which information(name, date, etc....):

1. After getting the coordinates of the text
2. Sort the coordinates of with respect to x-axis
3. In this way we can find which data belong to which label (for example, a text that comes after "permanent account number" is the account number)

To be done:
1. Make it work for jpeg and pdf (if pdf file is given, it should be converted into jpg and then processed)

2. Rotated image(if the image is rotated, it should to converted to appropriate angle so that tesseract understands it)

3. Government API integration