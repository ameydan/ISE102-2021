import math


def log_in_base(a, b):
    return math.log2(a) / math.log2(b)


def sum_all(a, b, c):
    return a + b + c


def swap(x, y):
    temp = y
    y = x
    x = temp


conv_factor = 1.8

''' 
    :param degree is used to get value of temperature
    :param conversion is used to indicate degree's unit. Default is fahrenheit
    :returns converted value
'''


def ftoc_converter(degree, conversion="F"):
    global conv_factor
    conv_factor = 2.3
    if conversion == "F":
        return (degree - 32) / conv_factor
    elif conversion == "C":
        return degree * conv_factor + 32


def find_nth(s, pattern, occurrance):
    count = 1
    pref_len = 0
    while count < occurrance:
        index = s.find(pattern)
        pref_len += len(s[:index + 1])
        s = s[index + 1:]
        count += 1
    return s.find(pattern) + pref_len


# Note 1: What if pattern doesn't repeat occurance times
# Note 2: What if I sen - as pattern
# Note 3: What if searching for a substring longer than 1
def find_nth_alternative(s, pattern, occurrance):
    count = 1
    while count < occurrance:
        index = s.find(pattern)
        s = s[:index] + "-" + s[index + 1:]
        count += 1
    return s.find(pattern)


def function_basics():
    print("*********Function basics*********")

    print(log_in_base(10, 2))
    print(sum_all(5, 3, 7))
    var = sum_all(11, 4 + 8 // 3, sum_all(2, 4, 6))
    a = 5
    b = 8
    swap(a, b)
    print(a, b)
    print("*********Function basics*********\n")


def named_param_and_scoping():
    print("*********Named parameters, scoping and globals*********")

    print(ftoc_converter(conversion="C", degree=30), "F")
    print(conv_factor)
    print("*********Named parameters, scoping and globals*********\n")


def find_nth_substr():
    print("*********Finding n_th occurrence of a substring*********")

    print(find_nth_alternative("ANANAS", "A", 3))

    print("*********Finding n_th occurrence of a substring*********\n")
