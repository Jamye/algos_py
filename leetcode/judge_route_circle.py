"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a
character. The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

# up left right down down left right up left down
#make a dictionary and count and make suree U and D are balanced

str1 = "ULRDURDLUDL"
str2 = "DURLRDULUDLRLRLUDUDRDL"
str3 = "UDRLRLUUUUUDDDR"
str4 = "DDUULLRR"
str5 = "UDLRUDLRUPLR"

def make_a_circle(direction_str):
    str_len = len(direction_str)
    counter = {"topdown":0, "leftright":0}

    if str_len %2 != 0:
        return "False"

    elif str_len %2 == 0:
        character_list = list(direction_str)

        for i in character_list:
            if i == "U":
                counter["topdown"] += 1
            elif i == "D":
                counter["topdown"] -= 1
            elif i == "L":
                counter["leftright"] += 1
            elif i == "R":
                counter["leftright"] -= 1

        if counter["topdown"] and counter["leftright"] != 0:
            return "False"
        else:
            return "True"


print(make_a_circle(str1))
print(make_a_circle(str2))
print(make_a_circle(str3))
print(make_a_circle(str4))
print(make_a_circle(str5))


#make a stack and go through push, pop and check for empty at the end
#won't work cause it will have to go through multiple times to get eerything

class Stack():
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()
