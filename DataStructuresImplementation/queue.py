class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        return self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue)==0:
            print("the queue is empty,no more element to dequeue")
            return None
        
        return self.queue.pop(0)
    
    def print_queue(self):
        print(self.queue)

    def empty_queue(self):
        return len(self.queue)==0

queue1=Queue()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
queue1.print_queue()

queue1.dequeue()
queue1.dequeue()
print("The remaining element in the queue is:")
queue1.print_queue()
queue1.dequeue()
queue1.dequeue()
queue1.print_queue()

