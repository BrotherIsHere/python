import pyautogui
import sys
import time

try:
    while True:
        pyautogui.rightClick(800,800)
        pyautogui.press('n')
        time.sleep(3)

except:
    sys.exit()

