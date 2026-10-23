class Product:
    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

class Inventory:
    def __init__(self):
        pass

    