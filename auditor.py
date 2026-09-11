inventory = 0
rejected = 0
stock = input("Please enter a stock: ")
while stock != "quit":
    if stock.isdigit() == False:
        print("Please enter a positive number")
        rejected += 1
    elif int(inventory) + int(stock) > 500:
        print("Warning: stock above 500")
        break
    else:
        inventory += int(stock)
    stock = input("Please enter a stock: ")

print("The total stock is: ",str(inventory), "\nRejected entries: ", str(rejected))