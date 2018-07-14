class Checkout:
    price = {}
    total = 0

    def __init__(self):
        self.price = {}
        self.total = 0

    def add_item_price(self, item, price):
        self.price[item] = price

    def add_item(self, item):
        self.total += self.price[item]

    def calculate_total(self):
        return self.total
