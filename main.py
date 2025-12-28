import pytesseract
import time
import difflib
import re

from config import Config
from screen import ScreenCapturer
from image_proc import ImagePreprocessor
from tts import Speaker



pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD


capturer = ScreenCapturer(Config.REGION)
processor = ImagePreprocessor(Config.TARGET_RGB, Config.COLOR_TOLERANCE)
speaker = Speaker(Config.TTS_RATE, Config.TTS_VOLUME)

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
                    speaker.speak(new_text)
                else:
                    speaker.speak(text)
                
            last_text = text
            
            time.sleep(1)
            
except KeyboardInterrupt:
    print("Остановка программы.")