import win32com.client


wim = win32com.client.GetObject("winmgmts:")
for usb in wmi.InstancesOf("Win32_LogicalDisk"):
