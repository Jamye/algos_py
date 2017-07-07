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


# create be_cheerful(). within it, console.log string "good morning!" call it 98 times

def be_cheerful():
    print("good morning!")

def many_times(num, run):
    for i in range(num + 1):
        run()

many_times(10, be_cheerful())
