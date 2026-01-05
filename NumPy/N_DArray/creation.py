import numpy as np 

#creating 2-D array ( 2 rows 3 coloumns)
arr_2d = np.array([[1,2,3],[4,5,6]])
print("2-D Array:")
print(arr_2d)


#creatinf 2d array with different data types
print("Array with different data types:")
array1=np.array([[1,2,3],['a','b','c'],[1.0,2.0,3.0]])
print(type(array1))


#creatig 3d array (2 blocks, 3 rows, 4 coloumns)
print("3-D Array:")
np_array = np.array([[[1, 2, 3, 4], 
                      [5, 6, 7, 8], 
                      [9, 10, 11, 12]],
                     [[13, 14, 15, 16], 
                      [17, 18, 19, 20], 
                      [21, 22, 23, 24]]])

print(np_array)


#emepty array 

print("Empty Array of 2D:")
empty_array = np.empty((3, 4))
print(empty_array)


print("Empty Array of 3D:")
empty_arr = np.empty((3,1,2))  #block, row , coloumn
print(empty_arr)


#prefilled array 
print("Prefilled Array of 2D with 7:")
prefilled_array = np.full((2, 3), 7)
print(prefilled_array)