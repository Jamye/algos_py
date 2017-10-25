"""
CTCI Page 90
1.2 Check Permutations

Given two strings, write a method to decide if one is a permutation of the other

"""
#This solution on the bottom only applies to strings that are the same length
def characters_check(some_str):
    new_dict = {}

    for i in some_str:
        if new_dict.has_key(i) is False:
            new_dict[i] = 1
        elif new_dict.has_key(i) is True:
            new_dict[i] = new_dict[i] + 1

    return new_dict

def permutation_checker(str_one, str_two):

    str_one_dict = characters_check(str_one)
    str_two_dict = characters_check(str_two)

    if str_one_dict == str_two_dict:
        print ("%s and %s are permutations" % (str_one, str_two))
    else:
        print ("Not permutations")


permutation_checker("god","ogd")
permutation_checker("hello","world")
permutation_checker("taco","coat")
permutation_checker("harry","potter")
