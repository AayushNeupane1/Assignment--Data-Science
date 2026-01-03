#creating array using the list 

import numpy as np 

list1=[1,2,3,4,5]
arr=np.array(list1)
print("Array created using list:",arr)

#taking input from the user
print("Enter elements of the array separated by space:")
# py_list=list(input().split())
# np_array=np.array(py_list)
# print("Using user input array:", np_array)

#from the scratch 

#using zeros() function 
arr_zeros=np.zeros((2,3))
print("Array of zeros:\n",arr_zeros)

#using arange function
arr_range=np.arange(10)
print("Array using arange function:",arr_range)


#difference between arange and linespace

array1 = np.arange(10,30,4)
array2 = np.linspace(10,30,4)

print("Using arange:", array1) 
print("Using linspace:", array2)


#random array creation 

rand_array=np.random.rand(3,2)
print("Random Array:\n",rand_array)

# array of length 5 with random integer values ranging from 1 to 100
rand_array = np.random.randint(1,100,size=5)
print("5 random integer values ranging from 1 to 100:", rand_array)