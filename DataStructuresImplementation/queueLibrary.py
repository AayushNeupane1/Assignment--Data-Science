from collections import deque

q=deque()

q.append(10)
q.append(20)
q.append(30)

print("The elements in the queue are",list(q))

for i in range(1,len(q)+1):
    item=q.popleft()
    print("The element to be dequeued is",item)
    print("The elements in the queue are",(q))

    if len(q)==0:
        print("Np more element to to be dequeue")
