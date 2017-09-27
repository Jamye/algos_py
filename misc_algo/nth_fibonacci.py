# Fibonacci
# Create a function to generate Fibonacci numbers.
# In this math sequence, each number is the sum of the previous two.

# def fibon(num):
#     fib_list = [0,1]
#     if num >= 2:
#         for i in range (2, num):
#             print (i-1) + (i -2)
#

def fibo(num):
    a = 1
    b = 1
    for i in range(num - 1):
        a = b
        b = a + b
    return a

# for i in range (1,10):
#     print fibo(i)

#using a while loop
def fibo2(num):
    first = 0
    second = 1
    i = 0

    while i < num:
        if i <= num:
            next_val = i
        else:
            next_val = first + second
            first = second
            second = next_val
        print(next_val)
        i = i + 1

print(fibo2(5))
