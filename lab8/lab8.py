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
    