

def add_to_clock(hour, min, sec, diff):
    sign = 1 if diff >= 0 else -1

    hour += (abs(diff)//3600)*sign
    diff = (abs(diff) % 3600)*sign
    min += (abs(diff) // 60)*sign
    diff = (abs(diff) % 60)*sign
    sec += diff

    if sign > 0:
        min += sec // 60
        sec %= 60

        hour += min // 60
        min %= 60

        hour %= 24

    if sec < 0:
        sec = 60 + sec
        min -= 1
    if min < 0:
        min = 60 + min
        hour -= 1
    if hour < 0:
        hour = 24 + hour

    return hour + ":" + min + ":" + sec


def collatz_seq(num, to_print=False):
    if to_print:
        print(num, end=" ")
    count = 0
    while num != 1:
        count = count +1
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3+1
        if to_print:
            print(num, end=" ")

    return count


def exercise01():
    print("********* Exercise 1*********")
    print(add_to_clock(23, 59, 59, 10))
    #print(add_to_clock(15, 42, 28, 3825))
    #print(add_to_clock(15, 42, 28, -3825))
    #print(add_to_clock(0, 0, 9, -10))
    #print(add_to_clock(23, 59, 59, 3662))
    print("*********Exercise 1*********\n")

def exercise02():
    print("********* Exercise 2*********")
    print(collatz_seq(485))
    print("*********Exercise 2*********\n")