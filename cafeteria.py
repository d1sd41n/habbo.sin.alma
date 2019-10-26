import numpy as np
import time
from vision import Vision
from controller import Controller
from habbo import BotHabbo
from random import shuffle
from random import randrange

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
            'floor2': 'assets/cafeteria/floor2.png',
            'floor3': 'assets/cafeteria/floor3.png',
            'drink1': 'assets/cafeteria/drink1.png',
            'drink2': 'assets/cafeteria/drink2.png',
            'drink3': 'assets/cafeteria/drink3.png',
        }

    def find_chair_and_sit(self):
        print("looking for a chair...")
        paths = self.get_images_path(self.static_templates, 'chair') # get al chair image paths
        shuffle(paths) # shuffle the list of paths to get random images
        return self.find_place_and_go(paths) # go to the chair if find one

    def find_floor_and_go(self):
        print("looking for a floor...")
        paths = self.get_images_path(self.static_templates, 'floor') # get al chair image paths
        paths.reverse()
        return self.find_place_and_go(paths) # go to the floor if find one


    def find_cafe_and_go(self):
        print("looking for a cafe...")
        paths = self.get_images_path(self.static_templates, 'drink')
        shuffle(paths)
        return self.find_drink_and_take_it(paths)



    def give_drink_to_some_habbo(self):
        """get a drink and give it to some habbo"""
        self.state = "looking for a drink"
        self.find_cafe_and_go()
        time.sleep(10)
        self.find_habbos_talking()
        time.sleep(1)
        self.find_and_open_habbo_menu()
        time.sleep(1)
        self.find_givedrink_button_and_click()



    def run(self):
        while True:
            time.sleep(30)
            if randrange(10)<=3:
                self.find_cafe_and_go()
                continue
            elif self.find_chair_and_sit():
                continue
            else:
                self.find_floor_and_go()




print("Charging vision library")
vision = Vision()
print("Charging controller library")
controller = Controller()
print("Charging bot")
bot = BotCafeteria(vision, controller)
# bot.find_floor_and_go()
# bot.find_chair_and_sit()
# bot.find_cafe_and_go()
# bot.run()
# bot.find_habbos_talking()
bot.give_drink_to_some_habbo()