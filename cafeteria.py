import numpy as np
import time
from vision import Vision
from controller import Controller
from habbo import BotHabbo
from random import shuffle

import cv2

class BotCafeteria(BotHabbo):
    def __init__(self, vision, controller):
        super().__init__(vision, controller)
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
        }

    def find_chair_and_sit(self):
        print("looking for a chair...")
        paths = list(self.static_templates.values())[:-1] # get all path chairs
        shuffle(paths) # shuffle the list of paths to get random images
        screen = self.vision.take_screenshot()
        for x in paths:
            template = self.vision.get_image(x)
            w, h = template.shape[::-1] # get weight, height of the image
            matches = self.vision.match_template(screen, template)
            print(matches)
            if len(matches):
                print("chair found")
                x, y = matches[0][0]+int(w/2), matches[0][1]+int(h/2)
                self.controller.set_mouse_position(x, y)
                self.controller.left_mouse_click()
                break
        time.sleep(1)
        self.find_x_and_close_object_window()

    def run(self):
        None
        # cv2.imshow('img_bgr', screen)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()



print("Charging vision library")
vision = Vision()
print("Charging controller library")
controller = Controller()
print("Charging bot")
bot = BotCafeteria(vision, controller)
bot.find_chair_and_sit()
#bot.run()
