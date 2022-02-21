import keyboard
from time import sleep
import json
import tkinter
import faulthandler

faulthandler.enable()


VALID_KEYS = "1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./\\"
KEYS_OPTION_SELECT = "1234567890-="

with open("keys_config.json") as config_file:
    CONFIG = json.load(config_file)
    key_delay = round(CONFIG["delay"] / 0.05)
    keys = CONFIG["keys"]


def run_on_press(key_info: keyboard.KeyboardEvent):
    if key_info.name not in VALID_KEYS:
        return
    for _ in range(key_delay):
        sleep(0.05)
        if not keyboard.is_pressed(key_info.name):
            return
    keyboard.press_and_release("backspace")
    input_win = tkinter.Tk()
    input_win.overrideredirect(1)
    input_win.geometry("500x50")
    input_win.geometry("-50-50")

    for each_item in keys[key_info.name]:
        tkinter.Label(input_win, text=each_item, width=len(each_item)).pack()

    input_win.mainloop()


keyboard.on_press(run_on_press)

sleep(10)  # why is this causing segmentation fault?
