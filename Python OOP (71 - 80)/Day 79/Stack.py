'''
    Write a class to represent a Stack with methods to push, pop, and check if the stack is empty.
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        '''Add an item to the top of the stack'''
        self.stack.append(item)

    def pop(self):
        '''Remove and return the item from the top of the stack'''
        if self.is_empty():
            raise IndexError("Cannot pop from the empty stack")
        return self.stack.pop()
    
    def is_empty(self):
        '''Check if the stack is empty'''
        return len(self.stack) == 0
    
    def peek(self):
        '''Return the number of items in the stack'''
        return len(self.stack)
    
    def __str__(self):
        '''String representation of the stack'''
        return str(self.stack)
    
# Example Usage
s = Stack()

print("is stack empty? ", s.is_empty()) # True
s.push(1)
s.push(2)
s.push(3)

print("Stack:", s) # [1,2,3]
print("Popped item:", s.pop())
print("Stack:", s) # [1,2]
print("Peek:",s.peek()) # 2
print("is stack empty?", s.is_empty()) # False

