import numpy as np

array1 = np.array([[1,2,-1,-2,3],
                   [1,2,3,-6,1]])

filter_arr= array1[array1 < 0]
print(filter_arr)

#replacing negative value with 0 
print("Before\n",array1)
print("Array after replacing negative values with 0:")
print(np.where(array1<0,0,array1))  #if condition is true replace with 0 else keep the same value
