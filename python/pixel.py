import pyautogui
import msvcrt
import pyHook
import pythoncom
import ctypes

def get_pixel():
    x,y=pyautogui.position()
    return pyautogui.pixel(x,y)

def OnKeyboardEvent(event):
    if event.Key=='backspace':
        return true
    else: False

mod=pyHook.HookManager()
mod.KeyAll=OnKeyboardEvent
mod.HookKeyboard()
pythoncom.PumpMessages(
while True:
    #print(msvcrt.getch())
    # if mod.HookKeyboard():
    #     pyautogui.moveTo(300,100)
    #     pyautogui.click(1)
    #     pyautogui.typewrite("Hello")
        # '''print('yes')'''
    print(mod.HookKeyboard())
