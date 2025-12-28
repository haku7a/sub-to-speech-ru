import pyttsx3


class Speaker:
    def __init__(self, rate, volume):
        self.rate = rate
        self.valume = volume

    def speak(self, text):
        if not text:
            return
        
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            engine.setProperty('valume', self.valume)

            engine.say(text)
            engine.runAndWait()

            del engine

        except Exception as e:
            print(f"Error TTS {e}")
        