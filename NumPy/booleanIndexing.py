#indexing in array using boolean 

import numpy as np
numbers_list = list(map(int,input().split()))
numbers = np.array(numbers_list)
odd_numbers =numbers[numbers%2!=0]
print(odd_numbers)



#modifying values using boolean indexing


numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numbers[numbers % 2==0]=0
print(numbers)

