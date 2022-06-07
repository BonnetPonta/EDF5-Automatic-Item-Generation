""" mission 87 の滝近くで放置
    後ろに下がりつつ、レイピアM4 を撃ち続ける
"""
from datetime import datetime
from time import sleep

from keyboard import is_pressed
from pyautogui import keyDown, keyUp, mouseDown, mouseUp


def script():
    while True:
        if is_pressed("Esc"):
            print(f"[{datetime.now()}] The Esc key is pressed and the process is terminated.")
            keyUp("s")
            mouseUp(button="left")
            break
        keyDown("s")
        mouseDown(button="left")


def main():
    print(f"[{datetime.now()}] Processing begins after 5 seconds...")
    sleep(5)
    script()


if __name__ == "__main__":
    main()
