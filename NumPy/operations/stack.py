import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print("array1:\n", array1)
print("array2:\n", array2)
 
result = np.stack((array1, array2))
print("Result:\n",result)