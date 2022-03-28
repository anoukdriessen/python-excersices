from tkinter import *

from pyparsing import col

window = Tk()
window.title("mile to km converter")
window.config(padx=20, pady=20)

def convert_mile_to_km():
    miles = entry.get()
    print(f"converting {miles} miles")
    km = round(float(miles) * 1.609, 3)
    equal_to_value.config(text=km)

entry = Entry()
entry.grid(row=0, column=1)
miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)
equal_to_value = Label(text="0")
equal_to_value.grid(row=1, column=1)
equal_to_label = Label(text="Km")
equal_to_label.grid(row=1, column=2)

calculate = Button(text="Calculate", command=convert_mile_to_km)
calculate.grid(row=2, column=1)

window.mainloop()