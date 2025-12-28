import pytesseract

class TextRecognizer:
    def __init__(self, tesseract_cmd, lang):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        self.lang = lang

    def image_to_text(self, image):
        try:
            text = pytesseract.image_to_string(image, lang=self.lang)
            return text.strip()
        except Exception as e:
            print(f"Error OCR: {e}")
            return ""

        