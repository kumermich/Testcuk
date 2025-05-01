############################
# Author: Sadegh Naderi
# Date created: 15.08.2023
# Path: BA23-14-Packages\report\Code\General\pdf2txt\pdf2txtIntroduction.py
# Version: 2
# Reviewed by: Sadegh Naderi
# Review Date: 15.08.2023
############################


import pdf2txt

def extract_text_from_pdf(pdf_path):
    try:
        # Create a PdfDocument instance
        pdf_document = pdf2txt.PdfDocument(pdf_path)

        # Initialize an empty dictionary to store the extracted text
        extracted_text_dict = {}

        # Iterate through each page and extract text
        for page_num in range(len(pdf_document.pages)):
            page = pdf_document.pages[page_num]
            page_text = page.extract_text()
            extracted_text_dict[f"Page {page_num + 1}"] = page_text.strip()

        return extracted_text_dict
    except Exception as e:
        print("An error occurred:", e)
        return None

# Specify the path to your PDF file
pdf_file_path = 'pdf/CVTemplate.pdf'

# Call the function to extract text
extracted_text_dict = extract_text_from_pdf(pdf_file_path)

# Export the results to a text file
output_file_path = 'output/extractedText.txt'

with open(output_file_path, 'w') as output_file:
    if extracted_text_dict:
        for page_num, page_text in extracted_text_dict.items():
            output_file.write(f"Page {page_num}:\n{page_text}\n\n")
    else:
        output_file.write("Text extraction failed.")
