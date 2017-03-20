import win32com.client
import os
import json
import pickle
import sys
def get():
    wmi = win32com.client.GetObject("winmgmts:")
    return [usb.name for usb in wmi.InstancesOf("Win32_LogicalDisk")]

before = get()
print(before)
print("______________________________________")
while True:
    after=get()
    print(after)
    print("______________________________________")
    input()
    if len(after)>len(before):
        drive=[usb for usb in after if usb not in before]
        print(drive)
        print("______________________________________")
        for item in drive:
            drives =[(dirname, subdirname,filenames) for dirname,subdirname, filenames in os.walk(item)]





        obj =pickle.dumps(drives,2)
        print(sys.getsizeof(obj))
        for i,b,c in pickle.loads(obj):
            print(i,"\t")
            for f in c:
                print(f,"\n")
