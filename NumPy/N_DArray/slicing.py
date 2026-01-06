import numpy as np

array1 = np.arange(1, 9)
# print(array1)
array1 = array1.reshape(2, 2, 2) #3d matrix where 2 matrix each of 2 row and 2 column

# slicing 3d array entirely
entire_array = array1[:, :, :]    
print("Entire Array:")
print(entire_array)
print(*"="*20)

#slicing second matrix 
second_matrix = array1[1, :, :]   
print("Second matrix:")
print(second_matrix)
print(*"="*20)


second_row_each_matrix = array1[:,1, :]   
print("\nSecond row of each matrix:")
print(second_row_each_matrix)
print(*"="*20)

second_column_each_matrix = array1[:, :, 1]    
print("\nSecond column of each matrix:")
print(second_column_each_matrix)