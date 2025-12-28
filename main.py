import time

from config import Config
from src.screen import ScreenCapturer
from src.image_proc import ImagePreprocessor
from src.tts import Speaker
from src.ocr import TextRecognizer
from src.text_logic import TextStreamProcessor


capturer = ScreenCapturer(Config.REGION)
processor = ImagePreprocessor(Config.TARGET_RGB, Config.COLOR_TOLERANCE)
speaker = Speaker(Config.TTS_RATE, Config.TTS_VOLUME)
recognizer = TextRecognizer(Config.TESSERACT_CMD, Config.LANG)
text_logic = TextStreamProcessor(Config.SIMILARITY_THRESHOLD)




def main():
    try:    
            while True:
                img = capturer.capture()
                filtered_img = processor.filter_color(img)
                raw_text  = recognizer.image_to_text(filtered_img)

                text_to_speak = text_logic.get_new_content(raw_text)


                
                if text_to_speak:
                    speaker.speak(text_to_speak)
                
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("Остановка программы.")
    finally:
        capturer.close()
    
if __name__ == "__main__":
    main()