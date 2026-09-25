class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


gasoline = Product("Regular Gasoline", 4, 5)

print(gasoline.total_value())