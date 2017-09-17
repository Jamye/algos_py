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

#reverse a string using a stack
def rev_string(my_str):
    z = Stack()                 #create new instance
    for i in my_str:
        z.push(i)               #create stack with data in reverse order
    new_string = ""
    while not z.is_empty():
        new_string += z.pop()   #while stack not empty, pop item and append to new string
    return new_string

#check to see if string is balanced
def is_balanced(symbol_string):
    checker_stack = Stack()
    if len(symbol_string) % 2 == 0:
        for i in symbol_string:
            if i == "(":
                checker_stack.push(i)
            elif i == ")":
                checker_stack.pop()
        if checker_stack.is_empty():
            return "Balanced"
        else:
            return "Not balanced"
    else:
        return "String length is odd"

print(is_balanced("(())"))

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
                index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

# print(par_checker('((())))')

# m = Stack()
# m.push('x')
# m.push('y')
# m.pop()
# m.push('z')
# print(m.peek())
