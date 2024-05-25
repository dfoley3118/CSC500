#!/usr/bin/env python3

# Importing the ItemsToPurchase class from the itemsToPurchase module
from itemsToPurchase import ItemToPurchase

# Importing the ShoppingCart class from shoppingCart modeul
from shoppingCart import ShoppingCart

# Import datetime to get current date
from datetime import datetime

#
# Program: onlineShoppingCart.py
# Author: Dennis Foley
# Date: May 25, 2023
#
# Main program to execute Online Shopping cart. Menu will be printed and each option will be 
# executed until the user enter q - Quit
#

#
# Print out menu options for online shopping cart
#
def print_menu(cart):
    print("\n          MENU")
    print(" a - Add item to cart")
    print(" r - Remove item from cart")
    print(" c - Change item quantity")
    print(" i - Output items' descriptions")
    print(" o - Output shopping cart")
    print(" q - Quit")
    choice = input("     Choose an option: ")
    return choice

def main():
    # Get the current date
    current_date = datetime.now()

    # Convert to string format
    date_string = current_date.strftime("%B %d, %Y")

    cart = ShoppingCart("Dennis Foley", date_string)
    choice = ""
    while choice != "q":
        choice = print_menu(cart)

        if choice == 'a':
            item_name = input("\nEnter name of item to purchase: ")
            item_price = float(input("Enter the price of the item: "))
            item_quantity = int(input("Enter the quantity of the item: "))

            # Creating an object of ItemToPurchase class for the item
            item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.add_item(item)
        elif choice == 'o':
            cart.print_total()

if __name__ == "__main__":
    main()
