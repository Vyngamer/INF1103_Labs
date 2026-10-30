# import whatever we need
import json
import os
import sys
from abc import ABC, abstractmethod

# create the product class 
class Product(ABC):
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
        print(f"ID: {self._prod_id} | Name: {self._name} | Price: ${self._price} | Stock: {self._stock}", end="")


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

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# create physicalproduct class
class PhysicalProduct(Product):
    def __init__(self, prod_id, name, price, stock, weight):
        super().__init__(prod_id, name, price, stock)
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self._weight}g")

    def get_fulfilment_info(self):
        print("Your product requires physical shipping")

# create a digitalproduct class
class DigitalProduct(Product):
    def __init__(self, prod_id, name, price, stock, download_size):
        super().__init__(prod_id, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        print(f" | Download Size: {self._download_size}MB")

    def get_fulfilment_info(self):
        print("Your product will be delivered digitally")




# # main function
# def main():
#     print("========================================")
#     print("INVENTORY MANAGEMENT SYSTEM")
#     print("========================================")
#     # load the inventory
#     inventory = load_inventory()
#     # display the menu
#     menu()
#     while True:
#         user_option = input("Enter option: ")
#         if user_option not in ["1","2","3","4","5","6"]:
#             print("Invalid option, try again")
#         elif user_option == '1':
#             inventory.display_all()
#         elif user_option == '2':
#             inventory.add_prod()
#         elif user_option == '3':
#             inventory.update_stock()
#         elif user_option == '4':
#             prod = inventory.search_prod()
#             if prod:
#                 print("\nProduct Found")
#                 print("-" * 50)
#                 prod.display_information()
#                 print("-" * 50)
#             else:
#                 print("\nProduct not found.")
#         elif user_option == '5':
#             inventory.save_inventory()
#         else:
#             print("Saving inventory before exit...")
#             inventory.save_inventory()
#             print("\nThank you for using Inventory Management System.")
#             print("Program terminated.")
#             sys.exit()

# main()

# prod1 = Product("P004", "Laptops", 1000, 200)
# prod1.display_information()

prod2 = PhysicalProduct("P004", "Laptops", 1000, 20, 200)
prod2.display_information()
prod2.get_fulfilment_info()

prod3 = DigitalProduct("P003", "Fifa", 10, 200, 20000)
prod3.display_information()
prod3.get_fulfilment_info()