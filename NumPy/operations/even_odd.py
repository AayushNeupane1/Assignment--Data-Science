import numpy as np

array1 = np.array(list(map(int, input().split())))

even_arr1 = array1[array1%2==0]

#replacing values of odd number with 0
even_arr2= np.where(array1%2==0,array1,0)

print(even_arr1)
print("Replaced odd number with 0:\n",even_arr2)