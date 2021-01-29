import tkinter
from tkinter import messagebox

Window = tkinter.Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

mybutton = tkinter.Button(Window, text ="Hello", command = helloCallBack)

mybutton.pack()
Window.mainloop()