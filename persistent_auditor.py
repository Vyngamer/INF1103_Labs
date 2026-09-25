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