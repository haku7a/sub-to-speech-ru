import pytesseract
from PIL import Image
import mss
import time
import pyttsx3
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'

REGION = {'left': 1400, 'top': 200, 'width': 1000, 'height': 800}

TARGET_RGB = (0, 255, 255)
COLOR_TOLERANCE = 30 

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
            
            img_array = np.array(img)
            target = np.array(TARGET_RGB)
            
            mask = np.all(np.abs(img_array - target) <= COLOR_TOLERANCE, axis=2)
            
            result_array = np.zeros_like(img_array) + 255
            result_array[mask] = [0, 0, 0] 
            
            filtered_img = Image.fromarray(result_array.astype('uint8'))
            
            filtered_img = filtered_img.convert('L')
            

            text = pytesseract.image_to_string(filtered_img, lang='rus+eng')
            text = text.strip()
            
            if text and text != last_text:
                print(text)
                
                speak_text(text)
                last_text = text
            
            time.sleep(1)
            
except KeyboardInterrupt:
    print("Остановка программы.")