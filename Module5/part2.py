#!/usr/bin/env python3

#
# Program: part2.py
# Author: Dennis Foley
# Date: May 18, 2023
#
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:
#
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
#
# This program will asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
#

# Ask the user for the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

points_awarded = 0
if (books_purchased == 0) or (books_purchased == 1):
    points_awarded = 0
elif (books_purchased == 2) or (books_purchased == 3):
    points_awarded = 5
elif (books_purchased == 4) or (books_purchased == 5):
    points_awarded = 15
elif (books_purchased == 6) or (books_purchased == 7):
    points_awarded = 30
elif (books_purchased >= 8):
    points_awarded = 60

# Display the number of points awarded
print(f"You have been awarded {points_awarded} points.")
