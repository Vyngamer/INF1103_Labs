import os

# function to save inventory
def save_inventory(new_entry):
    for i in new_entry:
        with open("orders.txt", "a") as inventory_file:
            inventory_file.write(i + "\n")