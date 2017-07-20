
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


#leap year
# write a function that determines whether a given year is a leap year. if a year is divisible by four,
# it is a leap year, unless it is divisble by 100. However, if it is divisible by 400, then it is
def leap_year(num):
    leap = False
    if num % 4 == 0:
        if num % 400 == 0:
            leap = True
        elif num % 100 == 0:
            leap = False
        else:
            leap = True
    return leap


#print and count
#print all integers multiples of 5, from 512 to 4096. Afterward, also log how many there were.
def print_and_count():
    count = 0
    for i in range(512, 4096):
        if i % 5 == 0:
            print (i)
            count = count + 1 
    return count


# multiples of 6
# print multiples of 6 up to 60,000 using a while
def multiples_of_six():
    count = 6
    while count <= 60000:
        print count
        count = count + 6
    return 


# counting the dojo way
# print integers 1 to 100. If divisible by 5, print "coding" instead. if by 10, also print "dojo"
def counting_dojo():
    for i in range (1,101):
        if i % 5 == 0:
            print "Coding"
        if i % 10 == 0:
            print "Dojo"


# what do you know?
# your funtion will be given an input parameter incoming. please print this value
def what_do_you_know(incoming):
    print incoming



# add odd integers from -11 to 11 and print the final sum, is there a short cut?
def meet_me_halfway():
    runner1 = -11
    runner2 = 11
    while runner1 < runner2:
        print runner1
        print runner2
        runner1 = runner1 + 2
        runner2 = runner2 - 2



# countdown by fours
# log positive numbers starting at 2016, counting down by fours(exclude 0), without a for loop
def count_down_four():
    number = 2016
    while number > 0:
        print number
        number = number - 4


# flexible countdown
# based on countdown by fours. given lowNum, highNum, mult, print mults from highNum to lowNum
def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print i

flex_countdown(1,12,3)