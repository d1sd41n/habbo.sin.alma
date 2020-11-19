from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyController

class Controller:
    """this module controlles the mouse and the keyboard"""
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyController()

    def set_mouse_position(self, x, y):
        self.mouse.position = (int(x), int(y)) # put the mouse in x, y coordinates

    def left_mouse_click(self):
        self.mouse.click(Button.left)

    def press_key_enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    # def release_key_enter(self):
    #     self.keyboard.release(Key.enter)

    def type_text(self, text):
        self.keyboard.type(text) # writes text where the cursor are
