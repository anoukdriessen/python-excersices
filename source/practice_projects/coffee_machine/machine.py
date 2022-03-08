class MenuItems:
    def __init__(self, name, water, milk, coffee, costs):
        self.name = name
        self.cost = costs
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Machine:
    def __init__(self):
        self.menu = [
            MenuItems(name="Latte", water=200, milk=150, coffee=24, costs=2.5),
            MenuItems(name="Espresso", water=50, milk=0, coffee=18, costs=1.5),
            MenuItems(name="Cappuccino", water=250, milk=50, coffee=24, costs=3),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
            print("Sorrty that item is unavailable")         

