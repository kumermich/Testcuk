import pdfplumber

# Define the file path and page number
pdf_path = "PdfplumberExample.pdf"
output_text_file = "Filtered_Text_Longest.txt"
debug_image_file = "Filtered_Text_Debug.png"
page_number = 1  # Specify the page to extract content from

def extract_and_debug_longest_text(pdf_path, page_number, output_file, debug_image_file):
    """
    @brief Extract the longest block of text from a PDF page, excluding tables and graphs,
           and visualize it in a debug image.

    @param pdf_path [in] Path to the PDF file.
    @param page_number [in] Page number to process (1-based index).
    @param output_file [out] File path to save extracted text.
    @param debug_image_file [out] File path to save the debug image highlighting the longest text.

    This function processes the specified PDF page, extracts the longest block of text
    while excluding text within tables and curve areas, and creates a debug image
    highlighting the extracted text.
    """
    with pdfplumber.open(pdf_path) as pdf:
        # Access the specified page
        page = pdf.pages[page_number - 1]

        # Extract bounding boxes for tables and curves
        table_bboxes = [table.bbox for table in page.find_tables()]
        curve_bboxes = []
        for curve in page.curves:
            x_coords = [pt[0] for pt in curve["pts"]]
            y_coords = [pt[1] for pt in curve["pts"]]
            bbox = (min(x_coords), min(y_coords), max(x_coords), max(y_coords))
            curve_bboxes.append(bbox)

        # Combine exclusion bounding boxes
        exclusion_bboxes = table_bboxes + curve_bboxes

        # Extract words from the page
        words = page.extract_words()

        # Filter words outside exclusion bounding boxes
        def is_outside_exclusion_bboxes(word):
            """
            @brief Check if a word is outside the exclusion bounding boxes.

            @param word Dictionary representing the word with bounding box coordinates.

            @return True if the word is outside all exclusion bounding boxes; False otherwise.
            """
            x0, y0, x1, y1 = word['x0'], word['top'], word['x1'], word['bottom']
            for bbox in exclusion_bboxes:
                bx0, by0, bx1, by1 = bbox
                if x0 < bx1 and x1 > bx0 and y0 < by1 and y1 > by0:
                    return False
            return True

        filtered_words = [word for word in words if is_outside_exclusion_bboxes(word)]

        # Group filtered words into lines and paragraphs
        paragraphs = []
        current_line = []
        prev_bottom = None

        for word in sorted(filtered_words, key=lambda w: w['top']):
            if prev_bottom is None or abs(word['top'] - prev_bottom) < 15:  # Adjust line spacing threshold
                current_line.append(word['text'])
            else:
                paragraphs.append(current_line)
                current_line = [word['text']]
            prev_bottom = word['bottom']

        if current_line:
            paragraphs.append(current_line)

        # Find the longest paragraph
        longest_paragraph = max(paragraphs, key=lambda line: len(" ".join(line))) if paragraphs else None

        # Create a debug image
        page_image = page.to_image()
        if longest_paragraph:
            for word_text in longest_paragraph:
                for word in filtered_words:
                    if word['text'] == word_text:
                        bbox = (word['x0'], word['top'], word['x1'], word['bottom'])
                        page_image.draw_rect(bbox, stroke="green", stroke_width=2)

            # Save the debug image
            page_image.save(debug_image_file)
            print(f"Debug image saved to {debug_image_file}")

            # Save the longest paragraph to a file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(" ".join(longest_paragraph))
            print(f"Longest text block saved to {output_file}")
        else:
            print("No text found outside tables and graphs.")

# Run the function
extract_and_debug_longest_text(pdf_path, page_number, output_text_file, debug_image_file)