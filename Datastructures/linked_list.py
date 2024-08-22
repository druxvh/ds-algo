class Node:
    '''
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    '''

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

# Linked list is a constant time operation
class LinkedList:
    '''
    Singly Linked List
    '''

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        '''
        Returns the number of nodes in the list
        Takes 0(n) time [Linear Time]
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        '''
        Adds new Node containing data at head of the list
        Takes 0(1) time [Constant Time]
        '''

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        Searches the value
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        '''
        Inserts a new Node containing data at the index postion
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time

        Takes overall O(n) time
        '''
        if index == 0:
            self.add(data)

        if index >  0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        '''
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        '''
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)





linkedL = LinkedList()
linkedL.add(1)
linkedL.add(2)
linkedL.add(3)
linkedL.add(4)
linkedL.insert(22, 1)
linkedL.remove(22)
print(linkedL)
