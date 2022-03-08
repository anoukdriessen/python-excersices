from machine import Machine
from brewer import Brewer
from cash import Cash

machine = Machine()     # handles logic
brewer = Brewer()       # makes the coffee
cash = Cash()           # handles the payment

turnedOn = True

while turnedOn:
    options = machine.get_items()
    choice = input(f"What would you like ({options})")
    if choice == "off":
        turnedOn = False
    elif choice == "report":
        brewer.report()
        cash.report()
    else:
        drink = machine.find_drink(choice)  
        if brewer.hasResources(drink) and cash.accept_payment(drink.cost):
            brewer.make_coffee(drink)      