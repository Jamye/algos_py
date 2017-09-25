class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext

# new_node = Node(93)
# print(new_node.get_data())

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    #sets new node as the new head (insert at front)
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


my_list = UnorderedList()
my_list.add(10)
some_list = [1, 5, 6, 'this', [1,3], {'hello': 3}]
my_list.add(some_list)
