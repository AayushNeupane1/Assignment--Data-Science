import numpy as np

a=np.array([9,12,21])
b=np.array([21,12,9])

# use of less()
result=np.less(a, b)
print(result)    

# use of less_equal()
result=np.less_equal(a,b)
print(result)  

# use of greater()
result = np.greater(a,b)
print(result)   

# use of greater_equal()
result=np.greater_equal(a, b)
print(result) 

# use of equal()
result = np.equal(a,b)
print(result)  

# use of not_equal()
result = np.not_equal(a,b)
print(result) 