"""
CTCI Page 90
1.1 is Unique

implement and algorithm to determine if string has all unique characters? What if
you cannot use additional data structures


"""

def is_unique(data):
    letter_dict = {}
    for i in data:
        if letter_dict.has_key(i) is False:
            letter_dict[i] = 1
            # print "%s is a unique letter" % i
        else:
            letter_dict.has_key(i) is True
            return ("Letter %s is repeated" % i)

    return ("Word %s has all unique characters" % data)

print(is_unique("pumpkin"))
print(is_unique("cracking"))
print(is_unique("blach"))
print(is_unique("doggie"))
print(is_unique("blue teapot"))
