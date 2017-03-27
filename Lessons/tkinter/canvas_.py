import tkinter as tk
x=y=None

def move(event):
    l.config(text=("{},{}").format(event.x,event.y))

def draw(e):
    global x,y
    if x is not None:
        c.create_line(x,y,e.x,e.y)
    x, y = e.x, e.y

def undraw(e):
    global x, y
    x=y=None

root=tk.Tk()
c=tk.Canvas(root,bg='white')
c.pack(fill=tk.BOTH,expand=1)
l=tk.Label(root, text='')
l.pack(side=tk.BOTTOM)

c.bind('<Motion>', move)
c.bind('<B1-Motion>', draw)
c.bind('<ButtonRelease-1>', undraw)
root.mainloop()
