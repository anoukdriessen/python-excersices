import tkinter
from tkinter import font
FONT = ("Roboto", 16, "bold")

# create a window
window = tkinter.Tk()
window.title("creating GUI's with tkinter")
window.minsize(width=666, height=333)

# create a label
myLabel = tkinter.Label(text="My name", font=FONT)
myLabel.pack(side="left") # add label to window

# create a mainloop
window.mainloop()