# import whatever we need
import json
import os
import sys

# create the product class 
class Product:
    def __init__(self, prod_id, name, price, stock):
        self._prod_id = prod_id
        self._name = name
        self._price = price
        self._stock = stock

    # function to update stock
    def update_stock(self, quantity):
        self._stock = int(quantity)
    
    # function to display info
    def display_information(self):
        print(f"ID: {self._prod_id} | Name: {self._name} | Price: ${self._price} | Stock: {self._stock}")


    def get_id(self):
        return self._prod_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def to_dict(self):
        return{
            "id": self._prod_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

# create the inventory class
class Inventory:
    def __init__(self):
        self.products = []

    # add prod function
    def add_prod(self):
        print("\nAdd new Product")
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
        prod = self.search_prod()
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
        print("products.json not found")
        print("Creating new json")
        with open("products.json", "w") as file:
            json.dump([], file)
        print("new json created")
    return inventory

# menu function to display the menu
def menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

# create physicalproduct class
class PhysicalProduct(Product):
    def __init__(self, prod_id, name, price, stock, weight):
        super().__init__(prod_id, name, price, stock)
        self._weight = weight

    def display_information(self):
        #print(f"ID: {self.__prod_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")
        print(f"ID: {self._prod_id} | Name: {self._name} | Price: ${self._price} | Stock: {self._stock} | Weight: {self._weight}")

# main function
def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    # load the inventory
    inventory = load_inventory()
    # display the menu
    menu()
    while True:
        user_option = input("Enter option: ")
        if user_option not in ["1","2","3","4","5","6"]:
            print("Invalid option, try again")
        elif user_option == '1':
            inventory.display_all()
        elif user_option == '2':
            inventory.add_prod()
        elif user_option == '3':
            inventory.update_stock()
        elif user_option == '4':
            prod = inventory.search_prod()
            if prod:
                print("\nProduct Found")
                print("-" * 50)
                prod.display_information()
                print("-" * 50)
            else:
                print("\nProduct not found.")
        elif user_option == '5':
            inventory.save_inventory()
        else:
            print("Saving inventory before exit...")
            inventory.save_inventory()
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            sys.exit()

main()