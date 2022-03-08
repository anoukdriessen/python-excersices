from machine import Machine
from brewer import Brewer
from cash import Cash

machine = Machine()
brewer = Brewer()
cash = Cash()

turnedOn = True

while turnedOn:
    options = machine.getItems()
    choice = input(f"What would you like ({options})")
    # if choice == "off":