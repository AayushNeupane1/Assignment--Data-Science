l_stack=[]

l_stack.append(10)
l_stack.append(20)
l_stack.append(30)
l_stack.append(40)

print("Stack after pushing and before poping",l_stack)

for i in range(len(l_stack)):
    rmv=l_stack.pop()
    print(f"Removed element from stack is",rmv)
    print(l_stack)
    if len(l_stack)==0:
        print("The stack is empty , no more emelemt can be popped")





