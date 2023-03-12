
from project.product import Product


class ProductRepository():
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product_to_check in self.products:
            if product_to_check.name == product_name:
                return product_to_check

    def remove(self, product_name):
        for product_to_check in self.products:
            if product_to_check.name == product_name:
                self.products.remove(product_to_check)
                break

    def __repr__(self):
        return '\n'.join([f'{p.name}: {p.quantity}' for p in self.products])
