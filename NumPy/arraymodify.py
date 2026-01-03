# Write a program to modify an array such that all even numbers and odd numbers are changed with user-specified integer input.

import numpy as np

numbers=np.array([1,2,3,4,5,6,7,8,9,10])
original=numbers.copy()

even_int=int(input("Enter even replacement: "))
odd_int=int(input("Enter odd replacement: "))

numbers[original % 2 == 0] = even_int
numbers[original % 2 != 0] = odd_int

print(numbers)
