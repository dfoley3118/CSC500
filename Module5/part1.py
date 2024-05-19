#!/usr/bin/env python3

#
# Program: part1.py
# Author: Dennis Foley
# Date: May 18, 2023
#
# This program will calculate the average rainfall over a period of years. 
# This program will ask for the number of years. For each year the program will prompt
# the user for the inches of rainfall for that month. 
#
# this program will display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
#

#
# Dictionary mapping month numbers to month names
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
# Enter the number of years
years = int(input("Enter the number of years: "))

total_rainfall = 0
total_months = years * 12

# iterates once for each year
for year in range(years):
    print(f"\nYear {year+1}:")
    # Loop over each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for {month_names.get(month)}: "))
        total_rainfall += rainfall

# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the results
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")
