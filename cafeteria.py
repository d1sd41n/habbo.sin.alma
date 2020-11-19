import numpy as np
import time
import glob
from habbo import BotHabbo
from random import shuffle
from random import randrange


class BotCafeteria(BotHabbo):
    def __init__(self):
        super().__init__()
        self.state = 'not started'
        self.floors = glob.glob("assets/rooms/{}/floor/*.png".format(self.room))
        self.chairs = glob.glob("assets/rooms/{}/chair/*.png".format(self.room))
        self.drinks = glob.glob("assets/rooms/{}/drink/*.png".format(self.room))
        print("ready...")

    def find_chair_and_sit(self):
        print("looking for a chair...")
        shuffle(self.chairs) # shuffle the list of paths to get random images
        return self.find_place_and_go(self.chairs) # go to the chair if find one

    def find_floor_and_go(self):
        print("looking for a floor...")
        shuffle(self.floors)
        return self.find_place_and_go(self.floors) # go to the floor if find one


    def find_cafe_and_go(self):
        print("looking for a cafe...")
        shuffle(self.drinks)
        return self.find_drink_and_take_it(self.drinks)



    def give_drink_to_some_habbo(self):
        """get a drink and give it to some habbo"""
        self.state = "looking for a drink"
        self.find_cafe_and_go()
        time.sleep(10)
        self.find_habbos_talking()
        time.sleep(1)
        self.find_and_open_habbo_menu()
        time.sleep(2)
        self.find_givedrink_button_and_click()



    def run(self):
        while True:
            print("waiting...")
            time.sleep(1)
            # self.find_cafe_and_go()
            # self.find_chair_and_sit()
            self.find_floor_and_go()
            # if randrange(10)<=10:
            #     self.find_cafe_and_go()
            #     if randrange(10)<=10:
            #         self.give_drink_to_some_habbo()
            #     continue
            # elif self.find_chair_and_sit():
            #     continue
            # else:
            #     self.find_floor_and_go()




print("Charging bot")
bot = BotCafeteria()
# bot.find_floor_and_go()
# bot.find_chair_and_sit()
# bot.find_cafe_and_go()
bot.run()
# bot.find_habbos_talking()
# bot.give_drink_to_some_habbo()