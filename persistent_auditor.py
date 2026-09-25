import os

# function to save inventory
def save_inventory(new_entry):
    for i in new_entry:
        with open("orders.txt", "a") as inventory_file:
            inventory_file.write(i + "\n")

def load_inventory():
    if not os.path.exists("orders.txt"):
        # create an empty file so future appends work
        open("orders.txt", "w").close()
        return []
    with open("orders.txt", "r") as inventory_file:
        inventory = inventory_file.read().splitlines()
    return inventory


# function to get product name
def get_product_name():
    prod_name = input("Enter Product Name: ")
    return prod_name

# get user input, both prod name and quantity
def get_quantity():
    while True:
        stock = input("Please enter a stock: ")
        if stock == "quit":
            save_inventory()
            break
        elif stock.isdigit() == False:
            print("Please enter a valid stock number")
        else:
            return int(stock)

# print out the current inventory
current_inventory = load_inventory()
if len(current_inventory) > 0:
    print("Current Inventory:\n")
    for i in current_inventory:
        print(i)
    print("\n")

# initialise the product id
if len(current_inventory) == 0:
    product_id = 1001
else:
    product_id = int(current_inventory[len(current_inventory) - 1].split(",")[0]) + 1

new_prod_lst = []
product_name = get_product_name()
while product_name != "quit":
    quantity = get_quantity()
    print("New Order Added:\n" + str(product_id) + "," + product_name + "," + str(quantity))
    new_prod = str(product_id) + ", " + str(product_name) + ", " + str(quantity)
    new_prod_lst.append(new_prod)
    product_id += 1
    product_name = get_product_name()

save_inventory(new_prod_lst)
print("Order successfully saved to orders.txt")