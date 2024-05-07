#
# Class: itemsToPurchase.py
# Author: Dennis Foley
# Date: May 7, 2023
#
# Class for Shopping Cart. Each object represent the item to purchased.
#
# Attributes
#     item_name: Name of the item to purchase
#     item_price: Price of the item
#     item_quantity: Quantity of the item to purchase

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def set_item_name(self, item_name):
        self.item_name = item_name
    
    def get_item_name(self):
        return self.item_name
        
    def set_item_price(self, item_price):
        self.item_price = item_price
    
    def get_item_price(self):
        return self.item_price

    def set_item_quantity(self, item_quantity):
        self.item_quantity = item_quantity
    
    def get_item_quantity(self):
        return self.item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")