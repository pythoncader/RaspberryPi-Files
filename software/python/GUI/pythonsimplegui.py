import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, World")

button = tk.Button(text="Click me!")

entry = tk.Entry(fg="yellow", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

name = entry.get()
print(name)
window.mainloop()
