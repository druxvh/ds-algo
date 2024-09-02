'''
Stacks by inheriting list class
'''

class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, item):
        self.append(item)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self)
    
    def insert(self, index, item):
        raise AttributeError("No attribute 'insert' in Stack")

dm = Stack()
dm.push(33)
print(dm.peek())