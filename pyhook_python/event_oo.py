import pyHook
import pythoncom

def OnMouseEvent(event):
    try:
        print(event.Position)
    except TypeError:
        print("rror")
    return True


mod=pyHook.HookManager()
mod.MouseAll=OnMouseEvent
mod.HookMouse()
pythoncom.PumpMessages()
