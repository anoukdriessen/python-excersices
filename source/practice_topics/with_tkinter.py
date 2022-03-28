from tkinter import *

FONT = ("Roboto", 16, "bold")

# create a window
window = Tk()
window.title("creating GUI's with tkinter")
window.minsize(width=666, height=333)

def click_button():
    print("I got clicked")
    # myLabel.config(text="Button has been clicked")
    myLabel.config(text=input.get())


# create an entry
input = Entry(width=60)
input.insert(END, string="Enter text and click on the button")
input.pack() # add entry to window

# create a button
button = Button(text="Click me", command=click_button, width=50)
button.pack() # add button to window

# create a label
myLabel = Label(text="Hello World", font=FONT)
myLabel.pack() # add label to window

# create multiline text entry
text = Text(height=5, width=50)
text.focus() # place the cursor in the textbox
text.insert(END, "Enter more text")
text.pack() # add text to window

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack() # add spinbox to window

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack() # add scale to window

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# create a mainloop
window.mainloop()