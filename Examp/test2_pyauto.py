from ctypes import windll
import time
import pyautogui

hdc = windll.user32.GetDC(0)
while True:
    x,y=pyautogui.position()
    #pixelColor = pyautogui.pyscreeze.screenshot().getpixel((x, y))
    #pixelColor=pyautogui.pixel(x,y)
    #print (pixelColor)
    color = windll.gdi32.GetPixel(hdc, x, y)
    print(color)
