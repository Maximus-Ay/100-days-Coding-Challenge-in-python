'''
    Write a Python class to represent a Binary Tree with methods for pre-order, in-order, 
    and post-order traversal.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self):
        '''Pre-order traversal: Root -> Left -> Right'''
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inorder(self):
        '''In-order traversal: Left -> Right -> Root'''
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.value, end=" ")
            node = node.right
    def postorder(self):
        '''Post-order traversal: Left -> Right -> Root'''
        stack = [(self.root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    print(node.value, end=" ")
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))


# Example Usage
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Pre-order traversal:")
tree.preorder() # Output: 1 2 3 4 5 

print("\nin-order traversal:")
tree.inorder() # Output: 4 2 5 1 3

print("\nPost-order traversal: ")
tree.postorder() # Output: 4 5 2 3 1
