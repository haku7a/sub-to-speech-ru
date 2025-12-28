import pytesseract
import time
import pyttsx3
import difflib
import re

from config import Config
from screen import ScreenCapturer
from image_proc import ImagePreprocessor



pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD


def speak_text(text):
    try:
        tts = pyttsx3.init()
        tts.setProperty('rate', Config.TTS_RATE)
        tts.setProperty('volume', Config.TTS_VOLUME)
        tts.say(text)
        tts.runAndWait()
        tts.stop()
        
    except Exception as e:
        print(f"Ошибка при произношении: {e}")

capturer = ScreenCapturer(Config.REGION)
processor = ImagePreprocessor(Config.TARGET_RGB, Config.COLOR_TOLERANCE)

try: 
        last_text = ""  
        
        while True:
            img = capturer.capture()
            filtered_img = processor.filter_color(img)
            
            text = pytesseract.image_to_string(filtered_img, lang=Config.LANG)
            text = text.strip()
            
            if text:
                similarity = difflib.SequenceMatcher(None, last_text, text).ratio()
                if last_text:
                    
                    if similarity >= 0.9:
                        last_text = text
                        continue
                
                print(text)
                
                if last_text and similarity <= 0.9:
                    start_index = 0
                    end_index = start_index + len(last_text)
                    new_text = text[end_index:].strip()
                    speak_text(new_text)
                else:
                    speak_text(text)
                
            last_text = text
            
            time.sleep(1)
            
except KeyboardInterrupt:
    print("Остановка программы.")