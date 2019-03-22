import cv2
from mss import mss
from PIL import Image
import numpy as np
import time



static_templates = {
    'left-goalpost': 'assets/left-goalpost.png',
    'bison-head': 'assets/bison-head.png',
    'pineapple-head': 'assets/pineapple-head.png',
    'bison-health-bar': 'assets/bison-health-bar.png',
    'pineapple-health-bar': 'assets/pineapple-health-bar.png',
    'cancel-button': 'assets/cancel-button.png',
    'filled-with-goodies': 'assets/filled-with-goodies.png',
    'next-button': 'assets/next-button.png',
    'tap-to-continue': 'assets/tap-to-continue.png',
    'unlocked': 'assets/unlocked.png',
    'full-rocket': 'assets/full-rocket.png'
}
# templates = { k: cv2.imread(v, 0) for (k, v) in static_templates.items() }
# def convert_rgb_to_bgr(img):
#         return img[:, :, ::-1]
# print(type(templates))
#
# for key, value in templates.items():
#     print(key)
#     print(9999999999999999999)
#     print(value)
#     scaled_template = cv2.resize(value, (0,0), fx=1.1, fy=1.1)
#     cv2.imshow(key, value)
#     cv2.imshow("scaled"+key, scaled_template)

#cv2.imshow('image', templates['left-goalpost'])

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
# screen = mss()
# frame = None
#
# sct_img = screen.grab(monitor)
# img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
# img = np.array(img)
# img = convert_rgb_to_bgr(img)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #print(img)
# cv2.imshow('image', img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(sct_img)
