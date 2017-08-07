# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a
# substring, "pwke" is a subsequence and not a substring.


def length_of_longest_substring(str):
    start = 0
    maxlen = 0
    new_dict = {}
    for i in range(len(str)):
        new_dict[str[i]] = -1
    for i in range(len(str)):
        if new_dict[str[i]] != -1:
            while start <= new_dict[str[i]]:
                new_dict[str[start]] = -1
                start += 1
        if i - start + 1 > maxlen:

length_of_longest_substring("hello World")