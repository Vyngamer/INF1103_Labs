# import whatever we need
import json
import os
import sys

# create the product class 
class Product:
    def __init__(self, prod_id, name, price, stock):
        self.__prod_id = prod_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # function to update stock
    def update_stock(self, quantity):
        self.__stock = int(quantity)
    
    # function to display info
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")


    def get_id(self):
        return self.__prod_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def to_dict(self):
        return{
            "id": self.__prod_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }


# create the inventory class
class Inventory:
    def __init__(self):
        self.products = []

    # add prod function
    def add_prod(self):
        print("/nAdd new Product")
        prod_id = input("Product ID: ")
        prod_name = input("Product Name: ")
        price = input("Price: ")
        stock = input("Stock Quantity: ")
        new_prod = Product(prod_id, prod_name, price, stock)
        self.products.append(new_prod)
        print("\nProduct added successfully")

    # search prod function
    def search_prod(self):
        print("\nSearch Product")
        prod_id = input("Enter Product ID: ")
        for prod in self.products:
            if prod.get_id() == prod_id:
                return prod
        return None

    # display all function
    def display_all(self):
        if len(self.products) == 0:
            print("Inventory is empty")
        else:
            print("\nCurrent Inventory")
            print("------------------------------------------------")
            for prod in self.products:
                prod.display_information()
            print("------------------------------------------------")

    # update stock function
    def update_stock(self):
        print("\nUpdate stock")
        prod_id = input("Enter Product ID: ")
        prod = self.search_prod(prod_id)
        if prod:
            print("\nProduct Found:")
            print("Name:", prod.get_name())
            print("Current Stock:", prod.get_stock())
            new_stock = input("\nNew Stock Quantity: ")
            prod.update_stock(new_stock)
            print("\nStock updataed successfully")
        else:
            print("\nProduct not found")
    
    # save inventory func
    def save_inventory(self):
        data = []
        for product in self.products:
            data.append(product.to_dict())
        with open("products.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nInventory saved successfully.")

# Load Inventory Function
def load_inventory():
    inventory = Inventory()
    if os.path.exists("products.json"):
        print("products.json found")
        with open("products.json", "r") as file:
            data = file.read()
            if data:
                products = json.loads(data)
                for item in products:
                    product = Product(item["id"], item["name"], item["price"], item["stock"])
                    inventory.products.append(product)
                print("Inventory loaded successfully.")
    else:
        with open("products.json", "w") as file:
            json.dump([], file)
    return inventory

# # menu function to display the menu
# def menu():
#     print("----------- MENU -----------")
#     print("1. Display All Products")
#     print("2. Add Product")
#     print("3. Update Stock")
#     print("4. Search Product")
#     print("5. Save Inventory")
#     print("6. Exit")
#     print("----------------------------")



# # main func
# def main():
#     inventory = load_inve