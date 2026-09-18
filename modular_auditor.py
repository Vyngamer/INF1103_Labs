# getting input function
def get_valid_input():
    stock = input("Please enter a stock: ")
    if stock == "quit":
        return "quit"
    elif stock.isdigit() == False:
        return "not_a_num"
    else:
        return int(stock)


# process delivery function
def process_delivery(current_total, new_value):
    return current_total + new_value


# calculate tax function
def calculate_tax(amount):
    return amount + (amount*0.10)


# generate report function
def generate_report(total_units, failed_attempts):
    print("The total stock is: ",str(inventory), "\nRejected entries: ", str(rejected))

# main code running area
inventory = 0
rejected = 0
still_valid = True

while still_valid:
    entry = get_valid_input()
    #print(entry)
    if entry == "not_a_num":
        print("Please enter a valid number")
    elif entry == "quit":
        generate_report(inventory, rejected)
        still_valid = False
    else:
        inventory = process_delivery(inventory, int(entry))