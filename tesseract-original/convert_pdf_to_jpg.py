# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('example.pdf',500,poppler_path=r'C:\Program Files\poppler-23.05.0\Library\bin')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('server/uploads/' + 'file1'+ str(i + 1) +'.jpg', 'JPEG')