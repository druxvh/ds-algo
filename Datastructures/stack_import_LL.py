from linked_list import *

class Stack(LinkedList):
    def __init__(self):
        self.mylist = LinkedList()
        self.item_count = 0
    
    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.mylist.del_first()
            self.item_count -= 1
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        return self.mylist.head.data
    
    def size(self):
        return self.item_count


'''

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())

'''  