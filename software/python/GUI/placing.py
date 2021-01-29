from tkinter import *
from tkinter import messagebox
top = Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text ="Hello", command = helloCallBack)

B.pack()
#B.place(height=100, width=100)
top.mainloop()

"""anchor − The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)

bordermode − INSIDE (the default) to indicate that other options refer to the parent's inside (ignoring the parent's border); OUTSIDE otherwise.

height, width − Height and width in pixels.

relheight, relwidth − Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

x, y − Horizontal and vertical offset in pixels."""