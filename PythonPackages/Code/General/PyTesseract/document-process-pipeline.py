import pytesseract
from PIL import Image
import cv2
import numpy as np
import logging
from pathlib import Path

class DocumentProcessor:
    """
    Handles end-to-end document processing and text extraction
    """
    def __init__(self, tesseract_path=None):
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        self.logger = logging.getLogger(__name__)

    def preprocess_image(self, image):
        """
        Applies preprocessing steps to improve OCR accuracy
        :param image: OpenCV image array
        :return: Preprocessed image array
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        # Denoise
        denoised = cv2.fastNlMeansDenoising(thresh)
        
        return denoised

    def extract_text_with_layout(self, image_path):
        """
        Extracts text while preserving document layout
        :param image_path: Path to the input image
        :return: Dictionary containing text and layout information
        """
        image = cv2.imread(str(image_path))
        preprocessed = self.preprocess_image(image)
        
        # Get detailed page analysis
        data = pytesseract.image_to_data(preprocessed, output_type=pytesseract.Output.DICT)
        
        # Extract text with positioning
        layout_info = []
        for i in range(len(data['text'])):
            if int(float(data['conf'][i])) > 60:
                layout_info.append({
                    'text': data['text'][i],
                    'confidence': data['conf'][i],
                    'bbox': (
                        data['left'][i],
                        data['top'][i],
                        data['width'][i],
                        data['height'][i]
                    ),
                    'block_num': data['block_num'][i],
                    'line_num': data['line_num'][i]
                })
        
        return layout_info