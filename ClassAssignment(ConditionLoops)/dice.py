# rolling dice 10 times using random.randint() and coutning number of 6

import random as r

def count_d():
    count=0
    for i in range(10):
        roll=r.randint(1,6)
        print(f"Number in dice while that was rolled {i+1} time:{roll}")
        if roll==6:
            count+=1

    return count


res=count_d()
print(f"There were total {res} occurance of 6")


