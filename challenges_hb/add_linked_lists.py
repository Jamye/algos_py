# Add Linked List

# Given two linked lists, treat as numbers and add them together.

class Node(object):

    def __init__(self, data=None, next_node=None, head=None):
        self.data = data
        self.head = head
        self.next_node = next_node
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, data):
        self.data = data

    def set_next_node(self, new_next):
        self.next_node = new_next


class Linked_list(object):
    def __init__(self, head=None):
        self.head = head
    
    def is_empty(self):
        return self.head == None

    def add(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()


my_list = Linked_list(12)
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
print(my_list)
