class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binarytree:

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

class Exterior:

    def print_leaves(self, root):
        if root:
            self.print_leaves(root.left)

            if root.left is None and root.right is None:
                print(root.data)

            self.print_leaves(root.right)

    def print_left(self, root):
        if(root):
            if root.left:
                print(root.data)
                self.print_left(root.left)
            elif root.right:
                print(root.data)
                self.print_left(root.left)
    
    def print_right(self, root):
        if(root):
            if root.right:
                print(root.data)
                self.print_left(root.right)
            elif root.left:
                print(root.data)
                self.print_left(root.right)

    def print_booundary(self, root):
        if root:
            print(root.data)
            self.print_left(root.left)
            self.print_leaves(root.left)
            self.print_leaves(root.right)
            self.print_right(root.right)

# Driver program to test above function 
root = Node(20) 
root.left = Node(8) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
root.right = Node(22) 
root.right.right = Node(25) 

# bt = Binarytree()
# bt.inorder(root) 
exbt = Exterior()
exbt.print_booundary(root)