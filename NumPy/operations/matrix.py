import numpy as np

array1=np.array([[1, 2], [3, 4]])
array2=np.array([[2, 0], [1, 2]])

print("Array multiplication: \n",array1*array2) 

#NumPy matrices
matrix1= np.matrix([[1, 2],[3, 4]])
matrix2 = np.matrix([[2, 0],[1, 2]])
print("Matrix multiplication:\n", matrix1 * matrix2)
print("Array power:\n",array1**2)  
print("Matrix power:\n",matrix1**2) 