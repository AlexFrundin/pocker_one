import pyautogui
import msvcrt
import pyHook
import pythoncom
import ctypes

def get_pixel():
    x,y=pyautogui.position()
    return pyautogui.pixel(x,y)

def OnKeyboardEvent(event):
    if event.Key==b'v':
        print('NO')
    else:
        print('yes')


mod=pyHook.HookManager()
mod.KeyAll=OnKeyboardEvent
mod.HookKeyboard()
pythoncom.PumpMessages()
