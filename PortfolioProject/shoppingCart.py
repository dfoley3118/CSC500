#
# Class: shoppingCart.py
# Author: Dennis Foley
# Date: May 25, 2023
#
# Class for Shopping Cart. Each object represent the item to purchased.
#
# Attributes
#   customer_name: Name of Customer
#   current_date: Current Date
#   car_items: List if items to purchase
#

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name
    
    def get_customer_name(self):
        return self.customer_name
        
    def set_current_date(self, current_date):
        self.current_date = current_date
    
    def get_current_date(self):
        return self.current_date
        
    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart")
    
    def modify_item(self, item):
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                if item.item_desc != "none":
                    self.cart_items[i].item_desc = item.item_desc
                if item.item_price != 0.0:
                    self.cart_items[i].item_price = item.item_price
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"          Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"            Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print()
            title = f"{self.customer_name}'s Shopping Cart - {self.current_date}"
            print(f"{title:^50}")
            print(f"{'Item Descriptions':^50}")
            for item in self.cart_items:
                item_desc = f"{item.item_name}: {item.item_desc}"
                print(f"{item_desc:^50}")

