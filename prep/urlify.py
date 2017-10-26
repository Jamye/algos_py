"""
CTCI Page 90
1.3 URLify:
Write a method to replace all spaces in a string with '%20'. You may assume that
the string has sufficient space at the end to hold additional characters, and
that you are given the "true" length of the string.

Input: "Mr John Smith      ", 13
Output: "Mr%20John%20Smith"

"""
def urlify(some_str):
    split_string = some_str.split()
    new_spaces = "%20"
    return new_spaces.join(split_string)

print urlify("hello world      this is too cruel     ")
print urlify("Mr John Smith       ")
print urlify("test    this URL ifier     ")
