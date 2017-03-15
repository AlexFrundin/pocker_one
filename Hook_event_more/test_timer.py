'''from threading import Timer
import time
import os
import win32api
import ctypes
import subprocess
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print (drives)

buff_size = ctypes.windll.kernel32.GetLogicalDriveStringsW(0,None)
buff = ctypes.create_string_buffer(buff_size*2)
print(ctypes.windll.kernel32.GetLogicalDriveStringsW(buff_size,buff))

print(filter(None, buff.raw.decode('utf-16-le').split(u'\0')))

print(os.getenv("J"))

mounted_letters = subprocess.Popen("wmic logicaldisk get name", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(mounted_letters.stdout.read())'''


import win32com.client

wmi = win32com.client.GetObject ("winmgmts:")

#for usb in wmi.InstancesOf ("Win32_UsbController"):
    #print ('Manufacturer: ' + str(usb.Caption))

#for usb in wmi.InstancesOf("Win32_DiskDrive"):
    #print(str(usb.Description))


#for usb in wmi.InstancesOf ("Win32_USBhub"):
    #print (usb.Caption)

dict_device = {item.Name:(item.VolumeName,item.VolumeSerialNumber) for item in wmi.InstancesOf("Win32_LogicalDisk")}
for item in dict_device:
    print(item.get())
