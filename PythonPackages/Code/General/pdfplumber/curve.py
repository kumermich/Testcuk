import pdfplumber

# Configuration
PDF_PATH = "PdfplumberExample.pdf"  # Path to the PDF file
PAGE_NUMBER = 1  # Page number to process (1-based index)
X_THRESHOLD = 200  # Minimum width for a valid curve
Y_THRESHOLD = 50  # Minimum height for a valid curve
CURVE_THICKNESS = 5  # Stroke width for debugging the detected curve

def extract_and_debug_curve(pdf_path, page_number, x_threshold, y_threshold, curve_thickness):
    """
    @brief Extract and debug the most likely valid curve from a PDF page.

    @param pdf_path Path to the PDF file.
    @param page_number Page number to process (1-based index).
    @param x_threshold Minimum width of the curve for validation.
    @param y_threshold Minimum height of the curve for validation.
    @param curve_thickness Stroke width for the curve in the debug image.

    This function processes a specified PDF page, filters valid curves based on
    dimensions, and visualizes the detected curve in a debug image.
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number - 1]
        curves = page.curves
        print(f"Extracted {len(curves)} curves on page {page_number}.")

        # Filter valid curves based on dimensions
        valid_curve = next(
            (curve for curve in curves if
             "pts" in curve and len(curve["pts"]) > 1 and
             max(pt[0] for pt in curve["pts"]) - min(pt[0] for pt in curve["pts"]) > x_threshold and
             max(pt[1] for pt in curve["pts"]) - min(pt[1] for pt in curve["pts"]) > y_threshold),
            None
        )

        if valid_curve:
            print("Valid curve found.")
            # Create a debug image
            page_image = page.to_image()
            page_image.draw_circles(valid_curve["pts"], radius=3, stroke="red", fill="white")
            page_image.draw_line(valid_curve["pts"], stroke="blue", stroke_width=curve_thickness)

            # Save the debug image
            debug_image_path = f"Page_{page_number}_Valid_Curve_Debug.png"
            page_image.save(debug_image_path)
            print(f"Debug image saved to {debug_image_path}")
        else:
            print("No valid curve found.")

# Run the function
extract_and_debug_curve(PDF_PATH, PAGE_NUMBER, X_THRESHOLD, Y_THRESHOLD, CURVE_THICKNESS)