import pdfplumber
import pandas as pd

# Define the file path and page number
pdf_path = "PdfplumberExample.pdf"  # Path to the PDF file
page_number = 1  # Specify the page to extract content from

# Table detection settings
table_settings = {
    "vertical_strategy": "lines",  # Use lines for vertical boundaries
    "horizontal_strategy": "lines",  # Use lines for horizontal boundaries
    "snap_tolerance": 2,  # Lower tolerance for snapping text to lines
    "join_tolerance": 1,  # Lower tolerance to avoid merging unrelated text
    "edge_min_length": 20,  # Minimum length for table edges
}

def extract_and_process_tables(pdf_path, page_number, table_settings):
    """
    @brief Extracts and processes tables from a specified page of a PDF.

    @param pdf_path Path to the PDF file.
    @param page_number Page number to process (1-based index).
    @param table_settings Dictionary containing table detection settings.

    This function extracts tables from a PDF page using specified settings, filters valid tables,
    and saves a debug image highlighting detected tables. It also processes and saves extracted
    tables as CSV files.
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number - 1]

        # Extract potential tables with bounding boxes
        detected_tables = []
        valid_bounding_boxes = []
        for table in page.find_tables(table_settings=table_settings):
            bbox = table.bbox  # Get bounding box of the detected table
            table_data = table.extract()

            # Ensure each row has at least one word (filter condition)
            if all(any(cell.strip() for cell in row) for row in table_data):
                detected_tables.append(table_data)
                valid_bounding_boxes.append(bbox)

        # Debugging visualization after filtering
        page_image = page.to_image()
        for bbox in valid_bounding_boxes:
            page_image.draw_rect(bbox, stroke="blue", stroke_width=2)
        debug_image_path = f"Page_{page_number}_Filtered_Table_Debug.png"
        page_image.save(debug_image_path)
        print(f"Filtered debug image saved to {debug_image_path}")

        # Process the extracted tables
        if detected_tables:
            for i, table in enumerate(detected_tables):
                print(f"\nDetected Table {i + 1}:")
                for row in table:
                    print(row)

                # Convert to DataFrame and clean data
                df = pd.DataFrame(table[1:], columns=table[0]).fillna("")  # First row as headers
                df.columns = df.columns.str.strip().str.replace("\n", " ")
                df = df.applymap(lambda x: x.strip().replace("\n", " ") if isinstance(x, str) else x)

                # Process rows to associate milestones with years
                current_year = None
                processed_data = []

                for _, row in df.iterrows():
                    year, milestone = row[0], row[1]
                    if year and not milestone:  # Update the current year
                        current_year = year
                        processed_data.append([current_year, None])
                    elif milestone:  # Append milestone with the current or new year
                        processed_data.append([current_year if not year else year, milestone])

                # Convert processed data to DataFrame
                processed_df = pd.DataFrame(processed_data, columns=["Year", "Milestone"])

                # Display and save the processed table
                print("\nProcessed Table:")
                print(processed_df)

                output_csv = f"Page_{page_number}_Processed_Table_{i + 1}.csv"
                processed_df.to_csv(output_csv, index=False)
                print(f"Processed table saved to {output_csv}")
        else:
            print("No valid table found on this page.")

# Run the function
extract_and_process_tables(pdf_path, page_number, table_settings)