import tkinter as tk
import urllib.request
import threading


is_stop= False

def start_job():
    b.config(text='Stop', command=stop_job)
    t=threading.Thread(target=get_url)
    t.start()

def stop_job():
    global is_stop
    is_stop=True
    b.config(text='Start', command=start_job)


def get_url():
    global is_stop
    for i in range(20):
        if is_stop:
            break
        r=urllib.request.urlopen('http://i.ua')
        print(len(r.read()))
    is_stop=False


root=tk.Tk()
b=tk.Button(text="Start", command=start_job)
b.pack()
root.mainloop()
