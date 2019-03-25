import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller

class Controller:
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = Controller()

    def set_mouse_position(x, y):
        self.mouse.position = (int(x), int(y))

    def left_mouse_click(self):
        self.mouse.click(Button.left)

    def press_key_enter(self):
        self.keyboard.press(Key.enter)

    def release_key_enter(self):
        self.keyboard.release(Key.enter)

    def type_text(self, text):
        self.keyboard.type(text)
