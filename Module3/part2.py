#!/usr/bin/env python3

#
# Program: part2.py
# Author: Dennis Foley
# Date: May 3, 2023
#
# This program will calculate what time an alarm will go off given the current time in hours and the number of hours to wait for the alarm
#

# Ask the user for the tim e now (in hours)
currentTime = int(input("Enter the current time (in hours): "))

# Ask the user for the number of hours to wait for the alarm
hoursToWait = int(input("Enter the number of hours to wait for the alarm: "))


# Calculate the total time after waiting
alarmTime = (currentTime + hoursToWait) % 24


# Display the alarm time
print(f"The alarm will go off at {alarmTime}:00 on a 24-hour clock.")

