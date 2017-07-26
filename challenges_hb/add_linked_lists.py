# Add Linked List

# Given two linked lists, treat as numbers and add them together.

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class Linked_list(object):
    def __init__ (self, head=None):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node


temp = Node(100)

print(temp.get_data())

