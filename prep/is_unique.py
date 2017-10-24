"""
CTCI Page 90
1.1 is Unique

implement and algorithm to determine if string has all unique characters? What if
you cannot use additional data structures


"""

def is_unique(data):
    letter_dict = {}
    for i in data:
        if letter_dict.has_key(i):
            print ("%s is not unique" % data)
        else:
            letter_dict[i] = i
            print ("Letter %s is not unique" % i)
    return

is_unique("pumpkin")
