'''
Doubly Linked List
'''
class Node:
    
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

    def __repr__(self):
        return "<Node data: %s>" % self.item
    
class DLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def insert_at_start(self, data):
        n = Node()
        n.item = data
        n.next = self.head
        
        #check if the list is not empty
        if not self.is_empty():
            self.head.prev = n
        self.head = n

    def insert_at_last(self, data):
        n = Node()
        n.item = data
        n.next = None
        if self.is_empty():
            self.head = n
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.prev = temp

    def insert_after(self, temp, data):
        '''temp is the node after which the data(that is new node) will be inserted'''

        #if no temp is given
        if temp is None:
            return 'Error, no temp is given'
        n = Node()
        n.item = data
        n.prev = temp               #temp is the node after which we've to insert our n node
        n.next = temp.next          #temp.next is the node next to temp

        if temp.next is not None:
            temp.next.prev = n
        temp.next = n
        

    def search(self, data):
        if self.is_empty():
            return 'Error, empty list'
        
        temp = self.head
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def print_all(self):
        all_nodes = []
        current_node = self.head
        while current_node:
            if current_node == self.head:
                all_nodes.append("[Head: %s]" % current_node.item)
            elif current_node.next is None:
                all_nodes.append("[Tail: %s]" % current_node.item)
            else:
                all_nodes.append("[%s]" % current_node.item)
            current_node = current_node.next
        return ' -> '.join(all_nodes)
    
    def del_first(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def del_last(self):

        if self.is_empty():
            return 'Error, empty list'
        
        if self.head.next == None:
            self.head = None
            return


        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.prev.next = None

    def del_item(self, data):
        if data is None or self.is_empty():
            return 'Error'

        temp =self.head
        while temp is not None:
            if temp.item == data:

                if temp.prev is None:       #if its head
                    self.head = temp.next
                    if self.head is not None:
                        self.head.prev = None
                    return
                
                if temp.next is None:       #if tail
                    temp.prev.next = None
                    return
                
                #if in the middle
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                return
            
            temp = temp.next
        return 'item not found'
    
    def __iter__(self):
        return DLL_Iterator(self.head)
    
class DLL_Iterator:
    '''
    Makes the doubly linket list iterable for loops
    '''
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
            
myList = DLL()
myList.insert_at_start(1)
myList.insert_at_last(10)
myList.insert_after(myList.search(1), 2)
myList.insert_after(myList.search(2), 3)
myList.insert_after(myList.search(3), 4)

# print(myList.print_all())


for x in myList:
    print(x, end=' ')

