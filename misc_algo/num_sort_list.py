#
# Segregate 0s and 1s in an array
# You are given an array of 0s and 1s in random order. Segregate 0s on left side
# and 1s on right side of the array. Traverse array only once.
#
# Example
# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def seperate_0_and_1(arr):
    my_list_len = len(arr)
    count = 0;

    for i in range(my_list_len):
        if(arr[i] == 0):
            count = count + 1
    print count

    for i in range(0, count):
        arr[i] = 0

    for i in range(count, my_list_len):
        arr[i] = 1

    return arr
my_arr = [0, 1, 0, 1, 1, 1, 0, 0]
print(seperate_0_and_1(my_arr))


#seperate an list with 0s at the front, 1s in the middle and 2s at the end

#helper swap function
def swap(arr, i1, i2):
  temp = arr[i1]
  arr[i1] = arr[i2]
  arr[i2] = temp

def sort_low_mid_high(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    #the loop will stop when mid idx > high,
    while mid <= high:
        #if item at mid is 0, swap with low and increment idx low and mid
        if arr[mid] == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1
        #if item at mid is 3, swap with the high and decrment high idx
        elif arr[mid] == 2:
            swap(arr, mid, high)
            high -= 1
        #if item at mid is 1, it will stay  in the middle,and increment mid idx
        elif arr[mid] == 1:
            mid += 1

    return arr

print sort_low_mid_high([2,2,2,0,0,0,1,1])


# Function to put all 0s on left and all 1s on right
# def segregate0and1(arr, size):
#     # Initialize left and right indexes
#     left, right = 0, size-1
#
#     while left < right:
#         # Increment left index while we see 0 at left
#         while arr[left] == 0 and left < right:
#             left += 1
#
#         # Decrement right index while we see 1 at right
#         while arr[right] == 1 and left < right:
#             right -= 1
#
#         # If left is smaller than right then there is a 1 at left
#         # and a 0 at right. Exchange arr[left] and arr[right]
#         if left < right:
#             arr[left] = 0
#             arr[right] = 1
#             left += 1
#             right -= 1
#
#     return arr
