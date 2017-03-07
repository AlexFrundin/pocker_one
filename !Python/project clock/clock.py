# -*- coding: utf-8 -*-
import tkinter
import time
def tick():
    global label#предоставляет доступ к переменой
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(1000,tick)

root=tkinter.Tk()
root.title("Часы")
root.geometry("500x150+100+100")#ширина высота отступы 
root.resizable(True,True)

label=tkinter.Label(root)
label.config(width="440",height="120",text="00:00:00",font="arial 100",fg="red")
label.pack()
label.after_idle(tick)
root.mainloop()#цикл запуска 
