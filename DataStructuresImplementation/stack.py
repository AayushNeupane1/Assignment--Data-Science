class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack)==0:
            print("The stack is empty, no more element to pop")
            return None
            
        return self.stack.pop()
        
    def print_stack(self):
        print(self.stack)

    def empty_stack(self):
        return len(self.stack)==0


stack1 = Stack()

stack1.push(10)
stack1.push(0)
stack1.push(25)
stack1.push(30)

stack1.print_stack()

stack1.pop()
stack1.pop()
stack1.print_stack()


stack2=Stack()

stack2.push(30)
stack2.push(10)

stack2.print_stack()

stack2.pop()
stack2.pop()
stack2.pop()
stack2.print_stack()
