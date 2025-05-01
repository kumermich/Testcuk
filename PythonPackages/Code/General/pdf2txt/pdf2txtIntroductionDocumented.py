"""! @brief Python program showcasing the extraction of text from a PDF document using the pdf2txt library."""
##
# @file pdf2txtIntroductionDocumented.py
#
# @brief This script demonstrates extracting text from a PDF document using the pdf2txt library.


############################
# Author: Sadegh Naderi
# Date created: 15.08.2023
# Path: BA23-14-Packages\report\Code\General\pdf2txt\pdf2txtIntroductionDocumented.py
# Version: 2.0
# Reviewed by: Sadegh Naderi
# Review Date: 02.09.2023
############################


##
# @file pdf2txtIntroductionDocumented.py
#
# @section description_of_file Description
# This script utilizes the pdf2txt library to extract text content from a specified PDF file. It defines a function
# 'extract_text_from_pdf' that processes each page of the PDF and stores the extracted text in a dictionary. The extracted
# text is then exported to a text file for further analysis.
#
# @section required_libraries Required Libraries
# The following library is imported for text extraction:
# - pdf2txt: A library for extracting text from PDF documents.
#   - For detailed documentation, visit: https://pypi.org/project/pdf2txt/
#
# @section author Author
# - Created by Sadegh Naderi on 15.08.2023.
# - Modified by Sadegh Naderi on 02.09.2023.
#

import pdf2txt

def extract_text_from_pdf(pdf_path):
    """! Extract text from a PDF document.
    
    This function takes the path to a PDF file as input and extracts text content from each page of the PDF. It utilizes
    the pdf2txt library to perform the extraction. The extracted text is stored in a dictionary, where the keys represent
    the page numbers and the values contain the extracted text.

    @param pdf_path The path to the PDF file to be processed.
    @return A dictionary containing extracted text for each page, or None if an error occurs during extraction.
    """
    try:
        # Create a PdfDocument instance

        ## @var pdf_document
        #  @brief A PdfDocument instance for processing a PDF file.
        #
        #  This variable holds an instance of the PdfDocument class provided by the pdf2txt library. It is used to open and
        #  process the specified PDF file, allowing text extraction from each page.
        pdf_document = pdf2txt.PdfDocument(pdf_path)

        # Initialize an empty dictionary to store the extracted text

        ## @var extracted_text_dict
        #  @brief A dictionary containing extracted text from each page of the PDF.
        #
        #  This dictionary holds the extracted text content from each page of the PDF file. The keys are in the format "Page n",
        #  where 'n' represents the page number, and the corresponding values contain the extracted text content from that page.
        #  If text extraction fails, this dictionary remains empty.
        extracted_text_dict = {}

        # Iterate through each page and extract text
        
        ## @var page
        #  @brief A PdfPage instance representing a single page of the PDF.
        #
        #  This variable holds an instance of the PdfPage class provided by the pdf2txt library. It represents a single page of
        #  the PDF file being processed. The `page` object is used to extract text content from the current page.
        
        ## @var page_text
        #  @brief Extracted text content from the current page of the PDF.
        #
        #  This variable holds the text content extracted from the current page of the PDF file. The `page_text` is a string
        #  containing the textual information present on the page, obtained using the `extract_text()` method of the PdfPage class.
        for page_num in range(len(pdf_document.pages)):
            page = pdf_document.pages[page_num]
            page_text = page.extract_text()
            extracted_text_dict[f"Page {page_num + 1}"] = page_text.strip()

        return extracted_text_dict
    except Exception as e:
        print("An error occurred:", e)
        return None

# Specify the path to your PDF file

## @var pdf_file_path
#  @brief Path to the PDF file for text extraction.
#
#  This variable holds the file path to the PDF document from which you want to extract text. You need to specify the path to
#  the PDF file in the format 'pdf/CVTemplate.pdf' (or the appropriate path). This path is used as an input parameter to the
#  `extract_text_from_pdf()` function for text extraction.
pdf_file_path = 'pdf/CVTemplate.pdf'

# Call the function to extract text

## @var pdf_file_path
#  @brief Path to the PDF file for text extraction.
#
#  This variable holds the file path to the PDF document from which you want to extract text. You need to specify the path to
#  the PDF file in the format 'pdf/CVTemplate.pdf' (or the appropriate path). This path is used as an input parameter to the
#  `extract_text_from_pdf()` function for text extraction.
extracted_text_dict = extract_text_from_pdf(pdf_file_path)

# Export the results to a text file

## @var output_file_path
#  @brief The path to the output text file where extracted text will be saved.
#
#  This variable holds the file path where the extracted text from the PDF pages will be saved. The extracted text
#  is organized and written to this file in a structured format. The path specifies the location and name of the
#  output text file for further reference or analysis.
output_file_path = 'output/extractedText.txt'

with open(output_file_path, 'w') as output_file:
    if extracted_text_dict:
        for page_num, page_text in extracted_text_dict.items():
            output_file.write(f"Page {page_num}:\n{page_text}\n\n")
    else:
        output_file.write("Text extraction failed.")
