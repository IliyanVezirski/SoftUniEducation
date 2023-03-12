from project.product import Product


class Drink(Product):
    def __init__(self, name: str, quantity=10):
        super(Drink, self).__init__(name, quantity)
