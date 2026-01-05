#subtracting on 1-D array
import numpy as np
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

first = np.array(list1)
second=np.array(list2)

# using - to subtract the second array from first
diff_ =first-second
print(diff_)

# using subtract() 
diff=np.subtract(first, second)
print(diff)

# multiplying on 1-D array

product = first*second
print(product)

# use the multiply() function to multiply two arrays
product = np.multiply(first,second)
print(product)

#comparsion operation on 1-D array

#use of equal to operator
result = first==second
print(result)

#use of less than or eqial to operator
result = first<=second
print(result)

#use of greater than equal to operator
result = first>=second
print(result)

#use of not euqal to operator 
result = first!=second
print(result)