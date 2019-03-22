import time
from pynput.mouse import Button, Controller as MouseController
import cv2

# mouse = MouseController()
# print(mouse.position)
# mouse.position = (0,0)

# mouse.Click(Button.left)
class Controller:
    def __init__(self):
        self.mouse = MouseController()
    def set_mouse_position(self, x, y):
            print(2222)
            self.mouse.position = (int(x), int(y))
    def smooth_move_mouse(self, from_x, from_y, to_x, to_y, speed=2):
        self.mouse.position = (from_x, from_y)
        self.mouse.click(Button.left)
        print(1111)
        steps = 40
        sleep_per_step = speed // steps
        x_delta = (to_x - from_x) / steps
        y_delta = (to_y - from_y) / steps
        for step in range(steps):
            new_x = x_delta * (step + 1) + from_x
            new_y = y_delta * (step + 1) + from_y
            self.set_mouse_position(new_x, new_y)
            time.sleep(sleep_per_step)
        self.mouse.position = (to_x, to_y)
        self.mouse.click(Button.left)
    def left_mouse_click(self):
        self.mouse.click(Button.left)

    def left_mouse_drag(self, start, end):
        self.move_mouse(*start)
        time.sleep(0.2)
        self.mouse.press(Button.left)
        time.sleep(0.2)
        self.move_mouse(*end)
        time.sleep(0.2)
        self.mouse.release(Button.left)
        time.sleep(0.2)


habbo = Controller()
while(True):
    #habbo.smooth_move_mouse(2172, 907, 2203, 916)
    print(1)
# habbo.smooth_move_mouse(2172, 907, 2203, 916)
