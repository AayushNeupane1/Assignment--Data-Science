# 8. Use array to store 100 integers efficiently.

import array 

int_Array=array.array('i', range(1,101))
for num in int_Array:
    print(num,end=',')
