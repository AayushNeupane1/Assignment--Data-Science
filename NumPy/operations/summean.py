import numpy as np

array1 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

sum_rows=np.sum(array1, axis=0)
print("Operation coloumn wise:")
print(sum_rows)

print("\n")

sum_rows=np.sum(array1, axis=1)
print("Operation row wise:")
print(sum_rows)

#average of first element of each row(axis 0)
mean_rows=np.mean(array1, axis=0)
print("Average along rows:")
print(mean_rows)