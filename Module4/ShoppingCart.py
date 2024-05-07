#!/usr/bin/env python3

# Importing the ItemsToPurchase class from the itemsToPurchase module
from itemsToPurchase import ItemToPurchase

#
# Program: ShoppingCart.py
# Author: Dennis Foley
# Date: May 7, 2023
#
# This program will implement an online shopping cart. The class ItemsToPurchase will be used to hold each item that is purchased.
#
# This version the user will be prompted for two items.  After the items have been entered the cost of the two
# items together will be displayed.
#

#
# Function to return boolean for Yes / No response
#
def string_to_boolean(string):
    if string.lower() == "yes":
        return True
    else:
        return False

# Create a list to store items to be purchased
shopping_cart = []

continue_shopping = True
while continue_shopping:
    # Prompting the user for the item to add to shopping cart
    print()
    item_name = input("Enter name of item to purchase: ")
    item_price = float(input("Enter the price of the item: "))
    item_quantity = int(input("Enter the quantity of the item: "))

    # Creating an object of ItemToPurchase class for the first item
    item = ItemToPurchase(item_name, item_price, item_quantity)
    shopping_cart.append(item)

    continue_shopping = string_to_boolean(input("\nContinue Shopping Yes/No: "))

# Calculate total cost of the shopping cart
total_cost = 0.0
for item in shopping_cart:
    total_cost += item.get_item_price() * item.get_item_quantity()

#
# Print out total cost and items in the shopping cart
#
print("\n       TOTAL COST")
for item in shopping_cart:
    item.print_item_cost()
print(f"       Total: ${total_cost}")
