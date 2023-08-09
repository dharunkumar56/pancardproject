from fpdf import FPDF

def convert_jpg_to_pdf(jpg_path, pdf_path):
    # Create a new PDF object
    pdf = FPDF()
    
    # Add a page with the same size as the image
    image_info = pdf.image(jpg_path)
    pdf.add_page(format=image_info['w'] > image_info['h'] and (image_info['w'], image_info['h']) or (image_info['h'], image_info['w']))
    
    # Set the image as the background of the page
    pdf.image(jpg_path, 0, 0, pdf.w, pdf.h)
    
    # Save the PDF file
    pdf.output(pdf_path)

# Path to the input JPG image
jpg_path = 'sample2.jpg'

# Output path for the PDF file
pdf_path = 'output_file.pdf'

# Convert JPG to PDF
convert_jpg_to_pdf(jpg_path, pdf_path)
