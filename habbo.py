import numpy as np
import time
from vision import Vision
from controller import Controller

import cv2

class BotHabbo:
    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'not started'
        self.static_templates_habbo = {
            'x_icon': 'assets/habbo/x_icon.png',
        }

    def find_x_and_close_object_window(self):
        """Looks for the X icon of a window and close it if find one"""
        print("looking for X window icon...")
        screen = self.vision.take_screenshot()
        path = self.static_templates_habbo['x_icon'] #get x icon path
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

# print("habbbbbbbbbbbbbbbbbb")
# print("Charging vision library")
# vision = Vision()
# print("Charging controller library")
# controller = Controller()
# print("Charging bot")
# bot = BotHabbo(vision, controller)
# bot.run()
