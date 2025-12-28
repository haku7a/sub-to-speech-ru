class Config:
    TESSERACT_CMD = r'C:\Program Files\Tesseract\tesseract.exe'
    REGION = {'left': 1400, 'top': 200, 'width': 1050, 'height': 500}
    TARGET_RGB = (0, 255, 255)
    COLOR_TOLERANCE = 30
    TTS_RATE = 180
    TTS_VOLUME = 2.0
    LANG = 'rus'
    SIMILARITY_THRESHOLD = 0.85