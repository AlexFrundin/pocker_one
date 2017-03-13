import pythoncom, pyHook

# def OnMouseEvent(event):
    #called when mouse events are received
    # print ('MessageName:',event.MessageName)
    # print ('Message:',event.Message)
    # print ('Time:',event.Time)
    # print ('Window:',event.Window)
    # print ('WindowName:',event.WindowName)
    # print ('Position:',event.Position)
    # print ('Wheel:',event.Wheel)



# return True to pass the event to other handlers
# return True

def OnKeyboardEvent(event):
    # if event.Key=='R':
        # print(event.MessageName)
        # print(event.Key)
    print ('MessageName:',event.MessageName)
    print ('Message:',event.Message)
    print ('Time:',event.Time)
    print ('Window:',event.Window)
    print ('WindowName:',event.WindowName)
    print ('Ascii:', event.Ascii, chr(event.Ascii))
    print ('Key:', event.Key)
    print ('KeyID:', event.KeyID)
    print ('ScanCode:', event.ScanCode)
    print ('Extended:', event.Extended)
    print ('Injected:', event.Injected)
    print ('Alt', event.Alt)
    print ('Transition', event.Transition)
    print ('---')
    return True


# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
# hm.MouseAll = OnMouseEvent
hm.KeyAll=OnKeyboardEvent
hm.HookKeyboard()
# set the hook
#hm.HookMouse()
# wait forever
pythoncom.PumpMessages()
