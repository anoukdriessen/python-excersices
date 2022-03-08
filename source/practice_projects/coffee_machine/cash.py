class Cash:
    CURRENTCY = "€"

    COIN_VALUES = {
        "vijf": 0.05,
        "tien": 0.10,
        "twintig": 0.20,
        "vijftig": 0.50,
        "een": 1.00,
        "twee": 2.00
    }

    def __init__(self):
        self.profit = 0
        self.money_in_machine = 0

    def report(self):
        print(f"Money: {self.CURRENTCY}{self.profit}")

    def process_coins(self):
        print("Insert money.")
        for coin in self.COIN_VALUES:
            self.money_in_machine += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_in_machine

    def accept_payment(self, cost):
        # True if accepted
        # False if insufficient
        self.process_coins()
        if self.money_in_machine >= cost:
            change = round(self.money_in_machine - cost, 2)
            print(f"Here is {self.CURRENTCY}{change} in change.")
            self.profit += cost
            self.money_in_machine = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_in_machine = 0
            return False    
