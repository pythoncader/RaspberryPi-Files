import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

def left_click(event):
    print("The button was left clicked!")
def right_click(event):
    print("The button was right clicked!")
def middle_click(event):
    print("The button was middle clicked!")

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

button = tk.Button(text="Click me!")
button.bind("<Button-1>", left_click)
button.bind("<Button-2>", middle_click)
button.bind("<Button-3>", right_click)
button.pack()
window.mainloop()