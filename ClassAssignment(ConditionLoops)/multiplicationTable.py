#multiplication of number and highlighting the multiple of 5 

n=int(input("Enter an integer:\n"))

def mul(n):
    for i in range(1,11):
        r=i*n
        if r%5==0:
            print(f"\033[1m{n}*{i}={r}\033[0m")
        else:
            print(f"{n}*{i}={r}")

       
        
mul(n)

