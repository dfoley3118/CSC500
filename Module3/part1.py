#!/usr/bin/env python3

#
# Program: part1.py
# Author: Dennis Foley
# Date: May 3, 2023
#
# This program calculates the total amount of a meal purchased at a restaurant. The program ask the user to enter the charge for the food 
# and then calculate the amounts with an 18 percent tip and 7 percent sales tax.
#

# Set tip amount to 18%
tipPercent = 0.18

# Set sales tax to 7%
taxPercent = 0.07

# Ask the user for the charge for the food
foodCharge = float(input("Enter the charge for the meal: $"))

# Calculate tip amount
tipAmount = foodCharge * tipPercent

# Calculate tax amount
taxAmount = foodCharge * taxPercent

# Calculate total cost
totalCost = foodCharge + tipAmount + taxAmount

# Display results
print("\n Bill Breakdown:")
print(f"    Food Charge: ${foodCharge:.2f}")
print(f"      Tip (18%): ${tipAmount:.2f}")
print(f" Sales Tax (7%): ${taxAmount:.2f}")
print(f"     Total Bill: ${totalCost:.2f}")
