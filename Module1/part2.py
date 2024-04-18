#!/usr/bin/env python3

input_str = input ("please enter a number: ")
num1 = int(input_str)
input_str = input ("please enter a second number: ")
num2 = int(input_str)

num3 = num1 * num2
print(num1, "*", num2, "=", num3)
if num2 == 0:
    print ("Division by 0 is not allowed")
else:
    num3 = num1 / num2
    print(num1, "/", num2, "=", num3)