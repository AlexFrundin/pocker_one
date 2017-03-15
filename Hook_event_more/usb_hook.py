import string
from ctypes import windll
import time
import socket

def main():
    before = set(get_drives())
    while True:
        after = set(get_drives())
        if len(after)>len(before):
            drives=after-before
            flag=True
        elif len(before)>len(after):
            drives=before-after
            flag=False
        else:
            drives=set()
        if len(drives):
            for drive in drives:
                if flag:
                    message=("{}".format(drive))
                    client((message,"connect"))
                    print(message)
                else:
                    message=("{}".format(drive))
                    client((message,"disconnect"))
                    print(message)
            before=after
        time.sleep(3)


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def client(message):
    s=socket.socket()
    name=socket.gethostname()
    s.connect(("192.168.0.88",5454))
    message=("{}||{}||{}||{}||".format(name,s.getsockname()[0], message[1], message[0]))
    s.sendall(message.encode("utf-8"))
    s.close()

if __name__ == '__main__':
    main()
