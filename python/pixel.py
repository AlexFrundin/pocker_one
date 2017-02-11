import pyautogui
import msvcrt
import pyHook
import pythoncom
import ctypes

'''
должен заметить, если запустить программу как pyw, она работает в фоном режиме и в диспетчере задач
отображается как пайтон32
сложно догодаться, что это она, пришлось убить ряд процессов связанных с пайтоном, чтобы прийти к пониманию , что это она
'''


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
