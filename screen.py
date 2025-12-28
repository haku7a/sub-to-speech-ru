import mss
from PIL import Image

class ScreenCapturer:
    def __init__(self, region):
        self.region = region
        self.sct = mss.mss()

    def capture(self):
        screenshot = self.sct.grab(self.region)
        return Image.frombytes("RGB", screenshot.size, screenshot.rgb)
    
    def close(self):
        self.sct.close()

        