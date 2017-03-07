from tkinter import *
def printer(event):
	label.config(text="Hello! I love Python")
root=Tk()
root.title("SecondPrint")
root.geometry("500x150+100+100")
label=Label(root)
label.config(width="440", height="100",font="arial 18",
text="Hello")
but=Button(root, text="Print",
			width=30,
			height=5,
			bg="white",
			fg="blue")
but.bind("<Button-1>",printer)
but.pack()
label.pack()
root.mainloop()