Archived... V1 is done; it works on windows. This is an super-tiny, old-ish project so it may not work well. It should mostly work on X on linux, but it probably won't work on wayland.

---

# hold for accents, symbols, and shortcuts
Because repeating the same key over and over is usually useless. Use useful accents, symbols, or text shortcuts instead.

A simple app to type accented characters (like à), symbols (like ‰), and configurable text shortcuts (like email, phone number, etc.). Just press and hold a key while the app is running.

![And something like this pops up on the bottom-right corner of your screen](https://user-images.githubusercontent.com/58201828/156706481-2399e8ac-29f5-49a5-91fd-1ef78780cc5b.png)

Then press the corresponding number key on your keyboard to insert!

---
### Download

For Windows, download the file from [GitHub Releases](https://github.com/blobbybilb/hold-for-accents-symbols-shortcuts/releases/tag/release) and, run the `.exe` inside. Edit the `key_config.json` file to edit what shows up for each key.

For Linux, clone or download the repository, make sure you have Python 3, the `keyboard` module, and `tkinter` installed. Then run `sudo python3 main.py` to run it.
- `sudo apt install python3-pip python3-tk` then `sudo python3 -m pip install keyboard` to install those

For macOS it may not work, but you can try it. Note that there is a built-in feature similar to this.
