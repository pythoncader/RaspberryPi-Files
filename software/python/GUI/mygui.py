# https://www.circuitbasics.com/how-to-create-user-interfaces/
# Object	Description
# App	The App object creates the main window of our GUI. This will contain all the widgets used within our GUI. app = App().
# ButtonGroup	This object creates a group of radio buttons, and the user can select a single option from the group. select = ButtonGroup(app, options=["mon", "tue", "wed","thurs", "fri"], selected="mon").
# CheckBox	The CheckBox object displays a checkbox that allows a user to tick or un-tick an option. checkbox = CheckBox(app, text="request leave")
# Box	
# Combo	This object displays a drop-down box that allows a user to select a single option from a list of options. combo = Combo(app, options=["mon", "tue", "wed","thurs", "fri"]).
# Drawing	Users can use this object to create visuals such as shapes, images, and text. drawing.rectangle(10, 10, 60, 60, color="blue")
# Listbox	The ListBox object displays a list of items from which users can select either a single or multiple items from the list. listbox = ListBox(app, items=["mon", "tue", "wed","thurs", "fri"]).
# Menubar	This object creates a menu at the top of the screen, with each menu option leading to a submenu.
# menubar = MenuBar(app, toplevel=["File", "Edit"], options=[ [ ["File option 1", file_function], ["File option 2", file_function] ], [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ] ])
# Picture	The Picture object displays an image. picture = Picture(app, image="test.gif")
# PushButton	This object displays a button that calls a function when pressed by a user. def display_msg(): print("This is our PushButton"). button = PushButton(app, command=display_msg)
# Slider	The Slider object displays a bar and selector, which users can use to specify a value in a range. slider = Slider(app).
# Text	This object displays text in our GUI. The text can be used to refer to titles, labels, and instructions. text = Text(app, text="Hello World").
# TextBox	This object allows users to type text in a box. mytextbox = TextBox(app)


from guizero import *
import sys

def button1pressed():
    print("Button 1 pressed")

def button2pressed():
    print("Button 2 pressed")

def button3pressed():
    print("Button 3 pressed")

def button4pressed():
    print("Button 4 pressed")

def exitprogram():
    print("Closed GUI")
    sys.exit()

app = App(title="Our GUI", width=700, height=300, layout="grid")
message = Text(app, text="Button 1:", grid=[0, 0])
message = Text(app, text="Button 2:", grid=[0, 1])
message = Text(app, text="Button 3:", grid=[0, 2])
message = Text(app, text="Button 4:", grid=[0, 3])

button1 = PushButton(app, command=button1pressed, text="Button 1", grid=[2, 0])
button2 = PushButton(app, command=button2pressed, text="Button 2", grid=[2, 1])
button3 = PushButton(app, command=button3pressed, text="Button 3", grid=[2, 2])
button4 = PushButton(app, command=button4pressed, text="Button 4", grid=[2, 3])
closebtn = PushButton(app, command=exitprogram, text="Close", grid=[4, 4])
app.display()
