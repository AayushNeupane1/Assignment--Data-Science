class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class linked_l:
    def __init__(self):
        self.head=None

    def create(self):
        node1=Node(10)
        self.head=node1

        node2=Node(20)
        node1.next=node2

        node3=Node(30)
        node2.next=node3

        node4=Node(40)
        node3.next=node4

ll1=linked_l()

ll1.create()

current_node=ll1.head

while current_node:
    print(current_node.data,end='-->')
    current_node=current_node.next

print("None")
        
    