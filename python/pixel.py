import pyautogui
import msvcrt
import pyHook
import pythoncom
import ctypes

def get_pixel():
    '''x,y=pyautogui.position()
    return pyautogui.pixel(x,y)'''
    pyautogui.moveTo(10,10)

def OnKeyboardEvent(event):
    print(event.Key)
    if event.Key=='Space':
        get_pixel()
    return True


mod=pyHook.HookManager()
mod.KeyAll=OnKeyboardEvent
mod.HookKeyboard()
pythoncom.PumpMessages()
