#!/usr/bin/env python3

"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
"""

user_input = input('Enter a series of numbers separated by commas. (Example: 34,67,55,33,12) Your input:').split(",")
# Note to future self: split() makes a list out of what would otherwise be a string...
user_input_tup = tuple(user_input)

print(user_input, '\n', user_input_tup)
