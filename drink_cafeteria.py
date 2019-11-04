import numpy as np
import time
from cafeteria import BotCafeteria
from random import shuffle
from random import randrange



class Drink_cafeteria(BotCafeteria):
    def __init__(self):
        super().__init__()




    def run(self):
        while True:
            print("waiting...")
            time.sleep(30)
            if randrange(10)<=3:
                self.find_cafe_and_go()
                if randrange(10)<=5:
                    self.give_drink_to_some_habbo()
                continue
            elif self.find_chair_and_sit():
                continue
            else:
                self.find_floor_and_go()




print("Charging bot")
bot = Drink_cafeteria()
# bot.find_floor_and_go()
# bot.find_chair_and_sit()
# bot.find_cafe_and_go()
bot.run()
# bot.find_habbos_talking()
# bot.give_drink_to_some_habbo()