import sys
import os
import json


def add_product(inventory, id, name, price, stock):
    new_prod = {
        "id": id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_prod)
    with open("products.json", 'w') as file:
        json.dump(inventory, file, indent=4)
    return 0

def update_stock():
    if os.path.exists("products.json"):
        with open("products.json", 'r') as file:
            data = file.read()
            if data:
                inventory = json.loads(data)
                prod_id = input("Enter the product ID to update stock: ")
                found = False
                for product in inventory:
                    if product['id'] == prod_id:
                        new_stock = input(f"Enter new stock for {product['name']}: ")
                        while new_stock.isdigit() == False:
                            print("Please enter a valid number for stock.")
                            new_stock = input(f"Enter new stock for {product['name']}: ")
                        product['stock'] = int(new_stock)
                        with open("products.json", 'w') as file:
                            json.dump(inventory, file, indent=4)
                        found = True
                        break
                if not found:
                    print("Product not found.")
            else:
                print("Inventory is empty.")
    else:
        print("No inventory file found.")
    return 0

def search_product():
    if os.path.exists("products.json"):
        with open("products.json", 'r') as file:
            data = file.read()
            if data:
                inventory = json.loads(data)
                search_id = input("Enter the product ID to search: ")
                found = False
                for product in inventory:
                    if product['id'] == search_id:
                        print(f"Product found: ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Stock: {product['stock']}")
                        found = True
                        break
                if not found:
                    print("Product not found.")
            else:
                print("Inventory is empty.")

def display_all():
    if os.path.exists("products.json"):
        with open("products.json", 'r') as file:
            data = file.read()
            if data:
                inventory = json.loads(data)
                print("Current Inventory:")
                for product in inventory:
                    print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Stock: {product['stock']}")
            else:
                print("Inventory is empty.")
    else:
        print("No inventory file found.")
    return 0

def load_inventory():
    if os.path.exists("products.json"):
        with open("products.json", 'r') as file:
            data = file.read()
            if data:
                inventory = json.loads(data)
                print("Inventory loaded successfully.")
            else:
                inventory = []
        return inventory
    else:
        inventory = []
        with open("products.json", 'w') as file:
            json.dump(inventory, file)
        return inventory
        

def save_inventory():
    if os.path.exists("products.json"):
        with open("products.json", 'r') as file:
            data = file.read()
            if data:
                inventory = json.loads(data)
                with open("products.json", 'w') as file:
                    json.dump(inventory, file, indent=4)
                print("Inventory saved successfully.")
            else:
                print("Inventory is empty. Nothing to save.")
    else:
        print("No inventory file found. Creating a new one.")
        with open("products.json", 'w') as file:
            json.dump([], file)
    return 0


def welcome_Screen():
    inventory = load_inventory()
    print("Please select an option:")
    print("1. Display all products")
    print("2. Add product")
    print("3. Update stock")
    print("4. search product")
    print("5. Save inventory")
    print("6. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            display_all()
        elif choice == '2':
            prod_id = input("Enter product ID: ")
            prod_name = input("Enter product name: ")
            price = input("Enter product price: ")
            stock = input("Enter product stock: ")
            while stock.isdigit() == False:
                print("Please enter a valid number for stock.")
                stock = input("Enter product stock: ")
            add_product(inventory, prod_id, prod_name, float(price), int(stock))
        elif choice == '3':
            update_stock()
        elif choice == '4':
            search_product()    
        elif choice == '5':
            save_inventory()
        elif choice == '6':
            save_inventory()
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")



welcome_Screen()