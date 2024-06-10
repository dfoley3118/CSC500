#!/usr/bin/env python3

# Importing the ItemsToPurchase class from the itemsToPurchase module
from itemsToPurchase import ItemToPurchase

# Importing the ShoppingCart class from shoppingCart modeul
from shoppingCart import ShoppingCart

#
# Program: onlineShoppingCart.py
# Author: Dennis Foley
# Date: June 9, 2023
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
    # Prompt the user for the customer's name
    customer_name = input("Enter customer's name: ")

    # Prompt the user for today's date
    todays_date = input("Enter today's date: ")

    # Output the customer's name and today's date
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {todays_date}")

    cart = ShoppingCart(customer_name, todays_date)
    choice = ""
    while choice != "q":
        choice = print_menu(cart)

        if choice == 'a':
            item_name = input("\nEnter the item name: ")
            item_desc = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))

            # Creating an object of ItemToPurchase class for the item
            item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
            cart.add_item(item)
        elif choice == 'r':
            item_name = input("\nEnter name of item to remove: ")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("\nEnter the item name: ")
            item_quantity = int(input("Enter the new quantity: "))
            newItem = ItemToPurchase(item_name, 0.0, item_quantity, "none")
            cart.modify_item(newItem)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()

if __name__ == "__main__":
    main()
