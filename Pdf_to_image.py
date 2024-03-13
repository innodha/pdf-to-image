import fitz
from PIL import Image
import os

# Specify the path to the folder containing PDF files
pdf_folder = "C:/Projects/Image_extraction/Orginal_doc/Highref_Pdf"

# Specify the output folder where JPG images will be saved
output_folder = "C:/Projects/Image_extraction/Pdf_to_folder"

# Set the desired DPI value
dpi = 1500

# Get a list of all PDF files in the input folder
pdf_files = [file for file in os.listdir(pdf_folder) if file.lower().endswith(".pdf")]

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each PDF file
for i, pdf_file in enumerate(pdf_files, start=1):
    # Create a subfolder for this PDF
    pdf_output_folder = os.path.join(output_folder, f"folder_{i}")
    os.makedirs(pdf_output_folder, exist_ok=True)

    # Open the PDF file
    pdf_path = os.path.join(pdf_folder, pdf_file)
    pdf = fitz.open(pdf_path)

    # Iterate through each page
    for j, page in enumerate(pdf):
        # Render the page as an image with specified DPI
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

        # Convert the image data to a PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image
        output_image_path = os.path.join(pdf_output_folder, f"page{j + 1}.jpg")
        img.save(output_image_path, dpi=(dpi, dpi))
        print(f"Saved high-quality image {output_image_path}")

    # Close the PDF file
    pdf.close()

print("Conversion complete!")
