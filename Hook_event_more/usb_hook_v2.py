import win32com.client
import time
import socket

def get_devices():
    wmi=win32com.client.GetObject("winmgmts:")
    return {item.VolumeSerialNumber:(item.Name,item.VolumeName) for item in wmi.InstancesOf("Win32_LogicalDisk")}

def main():
    before=get_devices()
    while True:
        after=get_devices()
        print(after)
        if len(after)>len(before):
            drives = [(item, after[item]) for item in after if item not in before]
            flag=True
        elif len(before)>len(after):
            drives=[(item, before[item]) for item in before if item not in after]
            flag=False
        else:
            drives=[]
        if drives:
            for disk in drives:
                if flag:
                    client((disk, "connect"))
                else:
                    client((disk, "disconnect"))
            before=after
        time.sleep(3)


def client(message):
    s=socket.socket()
    name=socket.gethostname()
    s.connect(("localhost",5000))
    message=("{}||{}||{}||{}||{}||{}".format(name,s.getsockname()[0], message[1], message[0][1][0], message[0][1][1], message[0][0]))
    s.sendall(message.encode("utf-8"))
    s.close()


if __name__ == '__main__':
    main()
