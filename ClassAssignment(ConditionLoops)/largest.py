n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))

def largest_num(a,b,c):
    largest=n1

    if b>largest:
        largest=b
    
    if c>largest:
        largest=c
    
    return largest

result=largest_num(n1,n2,n3)
print("The largest number is:",result)

