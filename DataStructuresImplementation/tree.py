class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def show(self):
        if self.left:
            self.left.show()

        if self.right:
            self.right.show()
            
        print(self.data)

root=Node(100)
r_left=Node(99)
r_right=Node(101)

root.left=r_left
root.right=r_right
root.show()
        