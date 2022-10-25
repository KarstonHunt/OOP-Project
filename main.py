class Item:
    def __init__(self, name, price, quantity):
        print(f"An instance created for: {name}\nPrice: {price}\nQuantity: {quantity}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Desktop", 1500, 5)


