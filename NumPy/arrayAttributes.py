import numpy as np

numbers = np.array([2, 4, 6, 8, 10, 12])

#array dimension
print('Number of dimensions:',numbers.ndim)

#shape of the array
print('Shape:',numbers.shape)


#data type of array elements
print('Data type of first array:',numbers.dtype)
float_numbers = np.array([3.2, 8.9, 12.0, 16.4])
print('Data type of second array:',float_numbers.dtype)

#size of an array

first = np.array([1,2,3,4,5,6])
second = np.array([2,4,6,8,10,12,14])

print('Size of first:',first.size)
print('Size of second:',second.size)