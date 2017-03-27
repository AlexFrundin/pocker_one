import tkinter as tk
import time



def f():
    l.config(bg='yellow')
    l.after(3000, g)

def g():
    l.config(bg='red')

def g_l():
    ll.config(bg='blue')

def f_l():
    ll.config(bg='grey')
    ll.after(3000,g_l)

root=tk.Tk()
l=tk.Label(root, text='Hello', bg="Red")
#размещаем на форме при помощи layout manager
l.pack(side=tk.LEFT,fill =tk.BOTH, expand='1')
ll=tk.Label(root,text="World",bg="Green").pack(side = tk.RIGHT,fill =tk.BOTH, expand='1')
b=tk.Button(root, text='ok', command =f).pack(fill=tk.BOTH,expand = '1')
b_ll=tk.Button(root, text="gree", command=f_l).pack(fill=tk.BOTH,expand='1')

l.after(3000, g)

root.mainloop()
