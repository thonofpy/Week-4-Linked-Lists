class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.a = []
        self.head = None

    def add(self, item):
        i = 0
        while i < 1:
            self.a.append(item)
            i += 1
        self.head = Node(item, self.head)

    def count(self):
        if self.is_empty():
            return 0
        else:
            return len(self.a)

    def contains(self, lists):
        if lists in self.a:
            return True
        else: 
            return False
    
    def remove(self): 
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.a.remove(item)
            self.head = self.head.next
            return item
    
    def is_empty(self):
        return self.head == None
