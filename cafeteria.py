import numpy as np
import time
from vision import Vision
from controller import Controller

import cv2

class BotCafeteria:
    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'not started'
        self.static_templates = {
            'chair2': 'assets/cafeteria/chair2.png',
            'chair3': 'assets/cafeteria/chair3.png',
            'chair4': 'assets/cafeteria/chair4.png',
            'chair5': 'assets/cafeteria/chair5.png',
            'chair6': 'assets/cafeteria/chair6.png',
            'chair7': 'assets/cafeteria/chair7.png',
            'chair8': 'assets/cafeteria/chair8.png',
            'chair9': 'assets/cafeteria/chair9.png',
            'chair10': 'assets/cafeteria/chair10.png',
            'floor1': 'assets/cafeteria/floor1.png',
            'x_icon': 'assets/cafeteria/x_icon.png',
        }

    def find_x_and_close_object_window(self, screen):
        print("looking for X window icon...")
        path = self.static_templates['x_icon']
        template = self.vision.get_image(path)
        matches = self.vision.match_template(screen, template)
        if len(matches):
            print("Closing window")
            x, y = matches[0][0], matches[0][1]
            self.controller.set_mouse_position(x, y)
            self.controller.left_mouse_click()

    def run(self):
        screen = self.vision.take_screenshot()
        self.find_x_and_close_object_window(screen)
        # cv2.imshow('img_bgr', screen)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()



print("Charging vision library")
vision = Vision()
print("Charging controller library")
controller = Controller()
print("Charging bot")
bot = BotCafeteria(vision, controller)
bot.run()
