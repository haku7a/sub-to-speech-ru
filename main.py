import pytesseract
from PIL import Image
import mss
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'

REGION = {'left': 0, 'top': 0, 'width': 500, 'height': 500}

try:
    with mss.mss() as sct:  
        last_text = ""  
        
        while True:
            screenshot = sct.grab(REGION)
            
            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            
            text = pytesseract.image_to_string(img, lang='rus+eng')
            text = text.strip()
            
            if text and text != last_text:
                print(text)
                last_text = text
            
            time.sleep(0.5)
            
except KeyboardInterrupt:
    print("Остановка программы.")