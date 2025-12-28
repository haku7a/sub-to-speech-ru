import pyttsx3


class Speaker:
    def __init__(self, rate, volume):
        self.rate = rate
        self.volume = volume

    def speak(self, text):
        if not text:
            return
        
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            engine.setProperty('volume', self.volume)

            engine.say(text)
            engine.runAndWait()

            del engine

        except Exception as e:
            print(f"Error TTS {e}")
        