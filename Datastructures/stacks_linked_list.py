'''
Stack using single linked list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.item_count = 0

    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        n = Node(data)
        n.next = self.top
        self.top = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.top
            self.top = self.top.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise self.is_empty()
        
    def size(self):
        return self.item_count
    
dm = Stack()
dm.push(1)
dm.push(2)
dm.push(22)
dm.pop()
print(dm.peek())