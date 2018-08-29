"""
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
from math import factorial
user_input = int(input("Enter a number. This program will compute the factorial of that number: "))
print(factorial(user_input))
