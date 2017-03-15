import pyHook
import pythoncom
from pyHook import cpyHook

#-*-coding: ISO-8859-1-*-


class HookEvent_():
    def __init__(self, msg, time, hwnd, window_name):
        '''Initializes an event instance.'''
        print("HookEvent++")
        self.Message = 512
        self.Time = time
        self.Window = hwnd
        self.WindowName = window_name

    def GetMessageName(self):
        '''
        @return: Name of the event
        @rtype: string
        '''
        return self.Message
    MessageName = property(fget=GetMessageName)


class MouseEvent_(HookEvent_):
    def __init__(self, msg=512, x=0, y=0, data=1, flags=1, time=1, hwnd=1, window_name=""):
        '''Initializes an instance of the class.'''
        print("MouseEvent++")
        HookEvent_.__init__(self, msg, time, hwnd, window_name)
        self.Position = (x,y)
        if data > 0: w = 1
        elif data < 0: w = -1
        else: w = 0
        self.Wheel = w
        self.Injected = flags & 0x01

class HookManager_():
    def __init__(self):
        self.mouse_funcs={}
        self.mouse_hook=False
    def __del__(self):
        self.UnhookMouse()


    def HookMouse(self):
        '''Begins watching for mouse events.'''
        cpyHook.cSetHook(14, self.MouseSwitch)
        self.mouse_hook = True


    def UnhookMouse(self):
        '''Stops watching for mouse events.'''
        if self.mouse_hook:
            cpyHook.cUnhook(14)
            self.mouse_hook = False


    def MouseSwitch(self, msg=512, x=0, y=0, data=1, flags=1, time=1, hwnd=1, window_name="Window"):
        try:
            print("1",self.mouse_funcs)
        except:
            print("2eroo")
        #print("msg: ",(msg))
        #print("x ",x)
        #print("y ",y)
        #print("data ",data)
        #print("flags ",flags)
        #print("time ",time)
        #print("hwnd ",hwnd)
        #print("window_name ",window_name)
        print("3yea")
        event = MouseEvent_(msg, x, y, data, flags, time, hwnd, window_name)
        func = self.mouse_funcs.get(msg)
        if func:
            return func(event)
        else:
            return True
            '''
        self.msg=msg
        try:
            self.event = MouseEvent_(msg, x, y, data, flags, time, hwnd, window_name)
            event=self.event
            self.msg=msg
        except:
            event=self.event
        finally:
            func = self.mouse_funcs.get(self.msg)
            if func:
                return func(event)
            else:
                return True


    def SubscribeMouseMove(self, func):
        if func is None:
            print("connect")
            self.disconnect(self.mouse_funcs, 0x0200)
        else:
            print("connect")
            self.connect(self.mouse_funcs, 0x0200, func)

    def SubscribeMouseAll(self, func):
        self.SubscribeMouseMove(func)

    MouseAll = property(fset=SubscribeMouseAll)

    def connect(self, switch, id, func):
        switch[id] = func

    def disconnect(self, switch, id):
        try:
            del switch[id]
        except:
            pass


def onMouseEvent(event):
    '''    print ('MessageName:',event.MessageName)
    print ('Message:',event.Message)
    print ('Time:',event.Time)
    print ('Window:',event.Window)
    print ('WindowName:',event.WindowName)
    print ('Position:',event.Position)
    print ('Wheel:',event.Wheel)
    print ('Injected:',event.Injected)
    '''
    try:
        print("4",event.Position)
    except TypeError:
        print("rror")
    return True

mod=HookManager_()

mod.MouseAll=onMouseEvent

mod.HookMouse()

pythoncom.PumpMessages()
