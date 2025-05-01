import pdfplumber
from PIL import Image

# Define constants for image filtering
MIN_WIDTH = 50  # Minimum width threshold for valid images
MIN_HEIGHT = 50  # Minimum height threshold for valid images

# File and page configuration
pdf_path = "PdfplumberExample.pdf"  # Path to the PDF file
page_number = 1  # Specify the page number to process

# Function to process and extract images from a PDF page
def process_pdf_images(pdf_path, page_number):
    """
    Process and extract images from a specified page of a PDF.

    @param pdf_path: str - Path to the PDF file
    @param page_number: int - Page number to process (1-based index)
    """
    with pdfplumber.open(pdf_path) as pdf:
        # Access the specified page
        page = pdf.pages[page_number - 1]

        # Extract images
        images = page.images
        print(f"Extracted {len(images)} potential images on page {page_number}.")

        # Create a debug image of the page
        page_image = page.to_image()

        # Draw bounding boxes around detected images for debugging
        for i, img in enumerate(images):
            bbox = (img['x0'], img['top'], img['x1'], img['bottom'])
            page_image.draw_rect(bbox, stroke="red", stroke_width=2)
            print(f"Image {i + 1}: {img}")

        # Save the debug image with bounding boxes
        debug_output_path = f"Page_{page_number}_Image_Debug.png"
        page_image.save(debug_output_path)
        print(f"Debug image saved to {debug_output_path}")

        # Filter and process valid images based on size thresholds
        valid_images = [
            img for img in images
            if (img['x1'] - img['x0'] > MIN_WIDTH) and (img['bottom'] - img['top'] > MIN_HEIGHT)
        ]

        print(f"Filtered {len(valid_images)} valid images on page {page_number}.")

        # Crop and save valid images
        for i, img in enumerate(valid_images):
            bbox = (img['x0'], img['top'], img['x1'], img['bottom'])
            cropped_image = page.within_bbox(bbox).to_image().original
            output_path = f"Page_{page_number}_Image_{i + 1}.png"
            cropped_image.save(output_path)
            print(f"Saved valid image {i + 1} to {output_path}")

        if not images:
            print("No potential images found on this page.")

# Run the function to process the PDF page
process_pdf_images(pdf_path, page_number)