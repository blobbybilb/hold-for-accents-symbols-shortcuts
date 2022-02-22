import keyboard
from time import sleep
import json
import tkinter
import threading


VALID_KEYS = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
KEYS_OPTION_SELECT = "1234567890-="

with open("keys_config.json", encoding='utf-8') as config_file:
    CONFIG = json.load(config_file)
    key_delay = round(CONFIG["delay"] / 0.05)
    keys = CONFIG["keys"]


def other_run_on_press(key_info: keyboard.KeyboardEvent):
    if key_info.name in KEYS_OPTION_SELECT:
        keyboard.write(keys[key_info.name][int(key_info.name)+])
    elif key_info.name == 'esc':
        input_win.destroy()

def checker():
    keyboard.on_press(other_run_on_press)


def run_on_press(key_info: keyboard.KeyboardEvent):
    if key_info.name not in VALID_KEYS:
        return
    for _ in range(key_delay):
        sleep(0.05)
        if not keyboard.is_pressed(key_info.name):
            return
    keyboard.release(key_info.name)
    keyboard.press_and_release("backspace")
    input_win = tkinter.Tk()
    input_win.overrideredirect(True)
    input_win.geometry("500x50")
    input_win.geometry("-50-50")

    items_for_this = keys[key_info.name]
    for each_item in items_for_this:
        print(each_item)
        tkinter.Label(input_win, text=each_item, width=5).pack(side="left")

    input_win.attributes("-topmost", True)

    checker_thread = threading.Thread(target=checker)
    input_win.mainloop()


keyboard.on_press(run_on_press)


keyboard.wait()
