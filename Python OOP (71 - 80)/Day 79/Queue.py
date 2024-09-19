'''
    Write a Python class to represent a Queue with methods to enqueue, dequeue, and check if the queue is empty.
'''

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        '''Add an item to the end of the queue'''
        self.queue.append(item)

    def dequeue(self):
        '''Remove and return the item from the front of the queue'''
        if self.is_empty():
            raise IndexError("Cannot dequeue from the end of an empty queue")
        return self.queue.pop(0)
    def is_empty(self):
        '''check if the queue is empty'''
        return len(self.queue) == 0

    def size(self):
        '''Return the number of items in the queue'''
        return len(self.queue)
    
    def peek(self):
        '''Return the item at the front of the queue without removing it'''
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self.queue[0]
    
    def __str__(self):
        '''String representation of the queue'''
        return str(self.queue)
    

# Let's try it
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue: ", q) # It should print[1,2,3]

print("Dequeued item: ", q.dequeue()) # 1

print("Queue: ", q)

print("Queue size:", q.size()) # 2

print("Peek:", q.peek()) # 2

print("Is the queue empty? ", q.is_empty()) # False


