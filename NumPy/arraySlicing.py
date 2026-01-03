import numpy as np

numbers = np.array(list(map(int,input().split())))

# slicing elements from index 1 to 4
sliced_numbers = numbers[1:4]
print(sliced_numbers)

# slicing elements from index 2 to last element
sliced_numbers = numbers[2:]
print(sliced_numbers)

# slicing elements from start to end without using any number
sliced_numbers = numbers[:]
print(sliced_numbers)