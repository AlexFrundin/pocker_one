import pyautogui
import os
import time
rgb=(0,0,0)
while True:
    x,y=pyautogui.position()
    print(x,y)
    '''if rgb==pyautogui.pixel(x,y):
        print("excellent")
        time.sleep(1)
        os.system('cls')
'''
