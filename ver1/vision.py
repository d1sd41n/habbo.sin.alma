import cv2
from mss import mss
from PIL import Image
import numpy as np
import time

class Vision:
    def __init__(self):
        resolution = mss().monitors[0]  # get the screen resolution
        self.monitor = {'top': 0, 'left': 0, 'width': resolution['width'], 'height': resolution['height']} # set the capture square
        self.screen = mss()

    def take_screenshot(self):
        sct_img = self.screen.grab(self.monitor) # take screeen shot
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb) # Creates a copy of an image memory from pixel data in a buffer.
        img = np.array(img) # convert the img in array
        img = self.convert_rgb_to_bgr(img) # convert the img to bgr
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert the img to black and white

        return img_gray

    def convert_rgb_to_bgr(self, img):
        return img[:, :, ::-1]

    def match_template(self, screen, template, threshold=0.9):
        """
        Matches template image in a target grayscaled image
        """
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED) # match template with screenshot
        matches = np.where(res >= threshold) # get the captures that superate the threshold
        matches = list(zip(*matches[::-1]))
        return matches

    def get_image(self, path):
        return cv2.imread(path, 0)
