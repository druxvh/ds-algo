class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self, data):
        self.items.insert(0,data)
    
    def insert_rear(self, data):
        self.items.append(data)
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque Empty")
        else:
            self.items.pop(0)
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque Empty")
        else:
            self.items.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque Empty")
        else:
            return self.items[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque Empty")
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    

'''
d = Deque()
d.insert_rear(11)
d.insert_front(22)
d.insert_front(32)
print(d.get_rear())
'''