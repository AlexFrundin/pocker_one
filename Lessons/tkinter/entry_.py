import tkinter as tk

def c():
    try:
        v1=v.get()
    except ValueError:
        e1.config(bg='red')
    try:
        v3=int(e3.get())
        v2=e2.get().strip()
        if v2 not in ("+","-","*","/"):
            raise ValueError
    except ValueError:
        tk.messagebox.showerror("Error","Invalid input")
        return
    if v2 == '+':
        res=v1+v3
    elif v2== '-':
        rex=v1-v3
    elif v2=='*':
        res==v1*v3
    else:
        res = v1/v3
    l.config(text=str(res))




def unred(e):
    e1.config(bg="white")



root =tk.Tk()

v=tk.IntVar()


e1 =tk.Entry(root, textvariable=v)
e1.grid(row=0, column=0)
e2 = tk.Entry(root ).grid(row=0,column=1)
e3=tk.Entry(root).grid(row=0,column=2)
b=tk.Button(root, 'Calc', command=c).grid(row=1,column=1)

l=tk.Label(root, text='').grid(row=1, column=1)
e1.bind('<FocusIn>',unred)
root.mainloop()
