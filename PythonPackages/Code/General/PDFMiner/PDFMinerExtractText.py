from pdfminer.high_level import extract_text
	
def extract_text_from_pdf(file_path):
	text = extract_text(file_path)
	return text
	
# Usage
pdf_file = 'sample.pdf'
output_file = 'output.txt'
	
text = extract_text_from_pdf(pdf_file)
with open(output_file, 'w', encoding='utf-8') as file:
	file.write(text)