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
    input_win.geometry("-50-50")
    input_win.attributes("-topmost", True)
    input_win.configure(bg='black')

    items_for_this = keys[key_info.name]
    for index, each_item in enumerate(items_for_this):
        tkinter.Label(input_win, text=each_item, width=len(each_item), font=("Helvetica", 20), bg='black', fg='light blue').grid(row=1, column=index)
        tkinter.Label(input_win, text=index+1, width=5, font=("Helvetica", 10), bg='black', fg='light grey').grid(row=2, column=index)

    input_win.update()
    while True:
        for i in KEYS_OPTION_SELECT:
            if keyboard.is_pressed(i):
                try:
                    if i == '0':
                        char_select = (items_for_this[9])
                    elif i == '-':
                        char_select = (items_for_this[10])
                    elif i == '=':
                        char_select = (items_for_this[11])
                    else:
                        char_select = (items_for_this[int(i) - 1])
                except IndexError:
                    input_win.destroy()
                    keyboard.press_and_release('backspace')
                    return
                input_win.destroy()
                keyboard.press_and_release('backspace')
                if keyboard.is_pressed('shift'):
                    keyboard.write(char_select.upper())
                else:
                    keyboard.write(char_select)
                return


keyboard.on_press(run_on_press)
print('Running: try pressing and holding a key!')
keyboard.wait()
