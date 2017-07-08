"""
Setting and swapping
set my_number to 42. set my_name to your name. Now swap my_number into my_name and vice versa

my_number = 42
my_name = 'James'

temp = my_number
my_number = my_name
my_name = temp

print(my_name)
print(my_number)
"""

"""
print -52 through 1066
def show_range():
    for i in range(-52, 1067):
        print(i)

show_range()
"""

"""
# create be_cheerful(). within it, console.log string "good morning!" call it 98 times

def be_cheerful():
    print("good morning!")

def many_times(num):
    for i in range(num + 1):
        be_cheerful()

many_times(10)
"""

# using for, print multiples of 3 from -300 to 0, skip -3 and -6

def multiple_of_three():
    for i in range(-300, 1):
        if i % 3 == 0 and i != -3 and i != -6:
            print (i) 

multiple_of_three()