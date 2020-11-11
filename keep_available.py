# Built-in Modules
import time

# Downloadable Modules
import pyautogui


# mouse position in tuple, (width-X, hight-Y).  Top-left part of screen is (0,0)
previous_position = pyautogui.position()

try:
    while True:
        time.sleep(57)
        current_position = pyautogui.position()
        if previous_position[0] == current_position[0] and previous_position[1] == current_position[1]:
            pyautogui.move(5, 5, .3)
            pyautogui.move(-5, -5, .3)
        previous_position = pyautogui.position()
        pyautogui.press('ctrl')
except KeyboardInterrupt:
    pass
