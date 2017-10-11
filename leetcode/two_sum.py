# Given an array of integers, return indices of the two numbers such that they add up to a
#  specific target.

# You may assume that each input would have exactly one solution, and you may not use the
#  same element twice.

#Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def two_sum(list,target):
    for i in list:
        for j in list:
            if i + j == target:
                temp = [list.index(j), list.index(i)]
    return temp

nums = [3, 2, 4]
print(two_sum(nums,6))
