class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def rev_string(my_str):
    z = Stack()                 #create new instance
    for i in my_str:
        z.push(i)               #create stack with data in reverse order
    new_string = ""
    while not z.is_empty():
        new_string += z.pop()   #while stack not empty, pop item and append to new string
    return new_string

print(rev_string("james"))



m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
# print(m.peek())
