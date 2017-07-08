
# Setting and swapping
# set my_number to 42. set my_name to your name. Now swap my_number into my_name and vice versa
def swap(name, number):
    my_number = number
    my_name = name

    temp = my_number
    my_number = my_name
    my_name = temp

    print my_name
    print my_number


# print -52 through 1066
def show_range():
    for i in range(-52, 1067):
        print(i)


# create be_cheerful(). within it, console.log string "good morning!" call it 98 times
def be_cheerful():
    print("good morning!")


def many_times(num):
    for i in range(num + 1):
        be_cheerful()


# using for, print multiples of 3 from -300 to 0, skip -3 and -6
def multiple_of_three():
    for i in range(-300, 1):
        if i % 3 == 0 and i != -3 and i != -6:
            print (i) 


# print integers 2000 to 5280 with while loop
def counter():
    count = 2000
    while count < 5280:
        print count
        count += 1


#if 2 given number represent your birth month and day in either order, log "how did you know?", else log "Just another day..."
def log_day(num1, num2):
    if num1 == 5 and num2 == 6:
        print ("how did you know?")
    elif num1 == 6 and num2 == 5:
        print ("how did you know?")
    else:
        print("Just another day ...")

