from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
	from pdfminer.converter import TextConverter
	from pdfminer.layout import LAParams
	from pdfminer.pdfpage import PDFPage
	from io import StringIO
	
	def extract_text_from_pdf(file_path):
	resource_manager = PDFResourceManager()
	text_output = StringIO()
	laparams = LAParams()
	
	with open(file_path, 'rb') as file:
	interpreter = PDFPageInterpreter(resource_manager, TextConverter(resource_manager, text_output, laparams=laparams))
	for page in PDFPage.get_pages(file):
	interpreter.process_page(page)
	
	text = text_output.getvalue()
	text_output.close()
	
	return text
	
	# Usage
	file_path = 'sample.pdf'
	text = extract_text_from_pdf(file_path)
	print(text)