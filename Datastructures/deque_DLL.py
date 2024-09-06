class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            n.next = self.front
            self.front.prev = n
            self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            n.prev = self.rear
            self.rear.next = n
            self.rear = n
        self.item_count += 1

    def del_front(self):
        if self.is_empty():
            raise IndexError("Deque Empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def del_rear(self):
        if self.is_empty():
            raise IndexError("Deque Empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1

    def get_front(self):
         if self.is_empty():
            raise IndexError("Deque Empty")
         else:
             return self.front.item
         
    def get_rear(self):
         if self.is_empty():
            raise IndexError("Deque Empty")
         else:
             return self.rear.item
         
    def size(self):
        return self.item_count
    
q = Deque()
q.insert_front(10)
q.insert_front(20)
q.insert_rear(30)
print(q.get_front())