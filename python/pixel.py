import pyautogui
import msvcrt
import pyHook
import pythoncom
import ctypes

'''
должен заметить, если запустить программу как pyw, она работает в фоном режиме и в диспетчере задач
отображается как пайтон32
сложно догодаться, что это она, пришлось убить ряд процессов связанных с пайтоном, чтобы прийти к пониманию , что это она
'MessageName:',event.MessageName
    print ('Message:',event.Message)
    print ('Time:',event.Time)
    print ('Window:',event.Window)
    print ('WindowName:',event.WindowName)
    print ('Ascii:', event.Ascii, chr(event.Ascii))
    print ('Key:', event.Key)
    print( 'KeyID:', event.KeyID)
    print ('ScanCode:', event.ScanCode)
    print ('Extended:', event.Extended)
    print ('Injected:', event.Injected)
    print ('Alt', event.Alt)
    print ('Transition', event.Transition)
    print ('---')

def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'

'''


def get_pixel():
        x,y=pyautogui.position()
        rgb=pyautogui.pixel(x,y)
        print(("position= {}, pixel={}").format((x,y),rgb))
        while True:
            if rgb != pyautogui.pixel(x,y):
                #print("Yee")
                #ctypes.windll.user32.keybd_event(0x20,0,0,0)#key,none, type if 0 keyDown, 0x0002 - keyDown
                #ctypes.windll.user32.keybd_event(0x20,0,0x0002,0)
                pyautogui.press(' ')

    #pyautogui.moveTo(10,10)
def KeyboardSwitch(event):
    '''
    считывает сначала keyDown, а потом KeyUp
    '''
    for item in dir(event):
        if '_' not in item:
            eval(('print("{0}= ",event.{0})').format(item))#чем заменить подобную конструкцию'''
    print('_-------_---------_---------')
    return True

def OnKeyboardEvent(event):
    try:
        print(event.Key)
    except TypeError:
        print("error")
    if event.Key=='Q':
        get_pixel()
    return True

mod=pyHook.HookManager()
#mod.KeyAll=OnKeyboardEvent
mod.KeyAll=KeyboardSwitch
#mod.KeyboardSwitch()
mod.HookKeyboard()
pythoncom.PumpMessages()
