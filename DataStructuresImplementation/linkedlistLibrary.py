from collections import deque

ll=deque()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Linked list:",list(ll))

print("popleft(element)->",ll.popleft())  
print("pop(element) ->",  ll.pop())           
print("Now list :", list(ll))

ll.append(50)
print("After adding to right :",list(ll))

ll.appendleft(60)
print("After adding to left :",list(ll))
