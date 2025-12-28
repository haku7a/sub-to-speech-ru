import numpy as np
from PIL import Image

class ImagePreprocessor:
    def __init__(self, target_rgb, tolerance):
        self.target_rgb = np.array(target_rgb)
        self.tolerance = tolerance

    def filter_color(self, img):
        img_array = np.array(img)
        mask = np.all(np.abs(img_array - self.target_rgb) <= self.tolerance, axis=2)
        result_array = np.zeros_like(img_array) + 255
        result_array[mask] = [0, 0, 0]
        return Image.fromarray(result_array.astype('uint8'))

        