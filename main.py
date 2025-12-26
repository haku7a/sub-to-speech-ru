import pytesseract
from PIL import Image
import mss
import time
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'

REGION = {'left': 1400, 'top': 410, 'width': 1000, 'height': 250}


def speak_text(text):
    try:
        tts = pyttsx3.init()
        
        tts.setProperty('rate', 180)
        tts.setProperty('volume', 2.0)
        
        tts.say(text)
        tts.runAndWait()
        
        tts.stop()
        
    except Exception as e:
        print(f"Ошибка при произношении: {e}")

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
                
                speak_text(text)
                last_text = text
            
            time.sleep(1)
            
except KeyboardInterrupt:
    print("Остановка программы.")