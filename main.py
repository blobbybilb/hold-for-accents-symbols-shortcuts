import keyboard
import time
import json

VALID_KEYS = "1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./\\"
print(set(VALID_KEYS))

with open("keys_config.json") as config_file:
    CONFIG = json.load(config_file)


def run_on_press(key_info: keyboard.KeyboardEvent):
    if key_info.name not in VALID_KEYS:
        return
    for _ in range(5):
        time.sleep(0.1)
        if not keyboard.is_pressed(key_info.name):
            print("nope")
            return
    print(key_info.name)
    print("held for half a second")


keyboard.on_press(run_on_press)


# def on_press(key: keyboard.KeyCode):
#     try:
#         if key.char not in VALID_KEYS:
#             return
#     except AttributeError:
#         return
#
#     print(key.char)
#
#
# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()
