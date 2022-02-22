import keyboard
from time import sleep
import json
import tkinter


VALID_KEYS = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
KEYS_OPTION_SELECT = "1234567890-="

with open("keys_config.json", encoding='utf-8') as config_file:
    CONFIG = json.load(config_file)
    key_delay = round(CONFIG["delay"] / 0.05)
    keys = CONFIG["keys"]


def check_for_press(text_options_list, the_win):
    while True:
        for i in KEYS_OPTION_SELECT:
            if keyboard.is_pressed(i):
                if i == '0':
                    keyboard.write(text_options_list[9])
                elif i == '-':
                    keyboard.write(text_options_list[10])
                elif i == '=':
                    keyboard.write(text_options_list[11])
                else:
                    keyboard.write(text_options_list[int(i)-1])
                the_win.destroy()



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
        tkinter.Label(input_win, text=each_item, width=5).pack(side="left")

    input_win.attributes("-topmost", True)
    input_win.update()
    print('hello')
    input_win.after(10, check_for_press, items_for_this, input_win)


keyboard.on_press(run_on_press)


keyboard.wait()
