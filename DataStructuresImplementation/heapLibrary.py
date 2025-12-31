from heapq import heappush, heappop, heapify

heap=[]
heappush(heap,-10) #heappush le element lai heap ma add garcha
heappush(heap,20)
heappush(heap,30)
heappush(heap,3)


print(heap)

print("Minimum value:", heappop(heap))  #headpop le chai minimum pop garcha
print(heap)

print("Minimum value:", heap[0])
print(heap)

arr=[1,5,3,2]
heapify(arr)
print(arr)