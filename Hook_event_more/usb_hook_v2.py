import win32com.client
import time
import socket

def get_devices():
    wmi=win32com.client.GetObject("winmgmts:")
    return {item.VolumeSerialNumber:(item.Name,item.VolumeName) for item in wmi.InstancesOf("Win32_LogicalDisk")}

def create_broadcast():
    udp_s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    udp_s.settimeout(2)
    return udp_s

def update_ip():
    with create_broadcast() as flood:
        flood.sendto("give_ip".encode('utf-8'),('255.255.255.255',4545))



def server_for_ip():
    pass

def main():
    before=get_devices()
    while True:
        after=get_devices()
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
    s.connect(("192.168.0.88",5454))
    message=("{}||{}||{}||{}||{}||".format(name,s.getsockname()[0], message[1], (message[0][1][0]+message[0][1][1]), message[0][0]))
    s.sendall(message.encode("utf-8"))
    s.close()


if __name__ == '__main__':
    while True:
        update_ip()
