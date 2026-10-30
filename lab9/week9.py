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

    def update_stock(self, quantity):
        self._stock = int(quantity)
    
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
        return {
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

    def calculate_shipping_cost(self):
        cost = float(self._weight) * 0.50
        print(f"The cost of delivery will be: ${cost:.2f}")
        
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self._weight
        return data


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

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self._download_size
        return data


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# create the inventory class
class Inventory:
    def __init__(self):
        self.products = []

    def add_prod(self):
        print("\nAdd new Product")
        prod_type = input("Enter Type (1 for Physical, 2 for Digital): ")
        
        if prod_type not in ['1', '2']:
            print("Invalid type selected. Returning to menu.")
            return

        prod_id = input("Product ID: ")
        prod_name = input("Product Name: ")
        price = input("Price: ")
        stock = input("Stock Quantity: ")
        
        if prod_type == '1':
            weight = input("Weight (g): ")
            new_prod = PhysicalProduct(prod_id, prod_name, price, stock, weight)
        else:
            download_size = input("Download Size (MB): ")
            new_prod = DigitalProduct(prod_id, prod_name, price, stock, download_size)
            
        self.products.append(new_prod)
        print("\nProduct added successfully")

    def search_prod(self):
        print("\nSearch Product")
        prod_id = input("Enter Product ID: ")
        for prod in self.products:
            if prod.get_id() == prod_id:
                return prod
        return None

    def display_all(self):
        if len(self.products) == 0:
            print("Inventory is empty")
        else:
            print("\nCurrent Inventory")
            print("------------------------------------------------")
            for prod in self.products:
                prod.display_information()
            print("------------------------------------------------")

    def update_stock(self):
        print("\nUpdate stock")
        prod = self.search_prod()
        if prod:
            print("\nProduct Found:")
            print("Name:", prod.get_name())
            print("Current Stock:", prod.get_stock())
            new_stock = input("\nNew Stock Quantity: ")
            prod.update_stock(new_stock)
            print("\nStock updated successfully")
        else:
            print("\nProduct not found")
    
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
                    # Instantiate the correct subclass based on the "type" attribute
                    if item.get("type") == "physical":
                        product = PhysicalProduct(
                            item["id"], item["name"], item["price"], 
                            item["stock"], item.get("weight", 0)
                        )
                        inventory.products.append(product)
                    elif item.get("type") == "digital":
                        product = DigitalProduct(
                            item["id"], item["name"], item["price"], 
                            item["stock"], item.get("download_size", 0)
                        )
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


# main function
def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    
    inventory = load_inventory()
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

if __name__ == "__main__":
    main()