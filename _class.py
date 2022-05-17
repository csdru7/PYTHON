import pyautogui as py
import time

print("wait for 5 secs")
time.sleep(5)


for i in range(10):
    py.write("hello")
    py.press("enter")
    time.sleep(1)