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

    def get_images_path(self, dict, image_type):
        """get a dictonionary and the type of image we want to filter the paths"""
        dictFiltered = {k:v for k,v in dict.items() if k.startswith(image_type)}
        paths = list(dictFiltered.values()) # get all path chairs
        return paths

    def find_place_and_go(self, image_paths):
        """get the image paths and for the coors in the screenshot
        and go to some place if find one"""
        screen = self.vision.take_screenshot()
        for x in image_paths:
            template = self.vision.get_image(x)
            w, h = template.shape[::-1] # get weight, height of the image
            matches = self.vision.match_template(screen, template)
            if len(matches):
                print("item found")
                x, y = matches[0][0]+int(w/2), matches[0][1]+int(h/2)
                self.controller.set_mouse_position(x, y)
                self.controller.left_mouse_click()
                time.sleep(1)
                self.find_x_and_close_object_window()
                return True
        return False
    
    def find_drink_and_take_it(self, image_paths):
        """get the image paths and for the coors in the screenshot
        and go to some place if find one"""
        screen = self.vision.take_screenshot()
        for x in image_paths:
            template = self.vision.get_image(x)
            w, h = template.shape[::-1] # get weight, height of the image
            matches = self.vision.match_template(screen, template)
            if len(matches):
                print("item found")
                x, y = matches[0][0]+int(w/2), matches[0][1]+int(h/2)
                self.controller.set_mouse_position(x, y)
                self.controller.left_mouse_click() # double click
                time.sleep(0.2)
                self.controller.left_mouse_click()
                time.sleep(1)
                self.find_x_and_close_object_window()
                return True
        return False

    def say_something(self, text):
        print("saying:",text)
        self.controller.type_text(text)
        self.controller.press_key_enter()

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
