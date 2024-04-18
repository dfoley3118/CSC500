#!/usr/bin/env python3

input_str = input ("Please enter a number: ")
num1 = int(input_str)
input_str = input ("Please enter a second number: ")
num2 = int(input_str)

print(num1, "*", num2, "=", num1 * num2)
if num2 == 0:
    print ("Division by 0 is not allowed")
else:
    print(num1, "/", num2, "=", num1 / num2)