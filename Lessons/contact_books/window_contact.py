import tkinter as tk
import ControllerContact as cc



def create():
    pass

def update():
    pass

def delete():
    pass

def read():
    pass

root=tk.Tk()

#root.geometry=(600,400, 100,100)

lb_name=tk.Label(text="Name:  ").grid(row=0,column=0)
name=tk.Entry().grid(row=0,column=1)

lb_name=tk.Label(text="Phone:  ").grid(row=1,column=0)
name=tk.Entry().grid(row=1,column=1)

bcreate=tk.Button(text="Create", command=create).grid(row=2, column=0)
#lb_hole_1=tk.Label(text="").grid(row=2,column=1)
bupdate=tk.Button(text="Update", command=update).grid(row=2, column=1)
bdelete=tk.Button(text="Delete", command=delete).grid(row=3,column=0)
bread=tk.Button(text="ReadAll", command=read).grid(row=3, column=1)



root.mainloop()
