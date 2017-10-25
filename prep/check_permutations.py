"""
CTCI Page 90
1.2 Check Permutations

Given two strings, write a method to decide if one is a permutation of the other

"""

def permutation_checker(str_one, str_two):
    letter_count = {}

    for i in str_one:
        if letter_count.has_key(i) is False:
            letter_count[i] = 1
        elif letter_count.has_key(i) is True:
            letter_count[i] = letter_count[i] + 1
    print letter_count

permutation_checker("hello","world")    
