import pyautogui
import keyboard
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0
autoClickerEnabled = False

# Set the clickInterval variable to how fast you want to click
clickInterval = 0.05

"""
Click Interval Status to get certain clicks per second:
.1 = 10 cps
.05 = 20 cps
.012 = 74 cps
.01 = 85 cps
.009 = 94 cps
"""

def enableAutoClicker():
    global autoClickerEnabled
    autoClickerEnabled = True
    print("autoclicker enabled")

def disableAutoClicker():
    global autoClickerEnabled
    autoClickerEnabled = False
    print("autoclicker disabled")

keyboard.add_hotkey("ctrl+|", enableAutoClicker)
keyboard.add_hotkey("ctrl+c", disableAutoClicker)

print("Press 'ctrl + |' to enable autoclicker")
print("Press 'ctrl + c' to disable autoclicker")
print("Press 'esc' to terminate autoclicker")

try:
    while True:
        if autoClickerEnabled:
            pyautogui.click(button='left')
            time.sleep(clickInterval)

        # Exit key
        if keyboard.is_pressed("esc"):
            print("Exiting program...")
            break

except KeyboardInterrupt:
    print("autoclicker has been terminated")

