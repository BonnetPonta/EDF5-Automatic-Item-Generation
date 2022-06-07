""" mission 87 の滝近くで放置
    後退しつつ、レイピア を撃ち続ける
"""
from datetime import datetime
from time import sleep, time

from keyboard import is_pressed
from pyautogui import keyDown, keyUp, mouseDown, mouseUp


class Colors:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    RESET = '\033[0m'


def log(msg):
    print(f"[{Colors.GREEN}{datetime.now()}{Colors.RESET}] {Colors.CYAN}{msg}{Colors.RESET}")


def end():
    log("The Esc key is pressed and the process is terminated.")
    keyUp("s")
    mouseUp(button="left")


def script():
    log("START!!")
    while True:
        if is_pressed("Esc"):
            end()
            break
        keyDown("s")
        mouseDown(button="left")


def main():
    log("Processing begins after 5 seconds...")
    sleep(5)
    script()


if __name__ == "__main__":
    start_time = time()
    try:
        main()
    except:
        end()
    finally:
        log(f"Time taken: {int(time()-start_time-5)} seconds")
