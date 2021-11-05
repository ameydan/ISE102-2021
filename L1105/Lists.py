def list_creation():
    a_list = [1, 2, 3, 4, 5]
    print(a_list)
    b_list = [i for i in range(5)]
    print(b_list)

def indexing_and_slicing():
    a_list = [1, 2, 3, 4, 5]
    print(a_list[3])
    print(a_list[2:4])
    print(len(a_list))
    for a in a_list:
        print(a, end=" ")

    c_list = [1, 2, "Tolga"]
    print(c_list[2][3])

    a_list[0] = 100
    print(a_list)
    a_list[0:3] = [100, 200, 300]
    print(a_list)

def list_operators():
    a_list = [10, 20, 30, 40, 50]
    b_list = [100, 90, 80, 70, 60]

    a_list += b_list

    print(a_list)
    print(b_list * 3)
    print(800 in a_list)

    a_list = [1, 2, 3]
    b_list = [4, 5]
    c_list = ["Tolga"]

    print(a_list + c_list)

    a_list.append(b_list)
    print(a_list)

def list_methods():
    a_list = [5, 4, 3, 2, 1]
    a_list.append(6)
    a_list.remove(3)
    #a_list.remove(a_list[4])
    del a_list[0]
    print(a_list)
    print(a_list.index(6))
    print(sorted(a_list))
    a_list.sort()
    print(a_list)
    a_list.reverse()
    print(a_list)
    a_list.insert(2, 5)
    print(a_list)


def swap_val(a, b):
    return b, a


def tuples():
    a_tuple = (5, 3, 1, 7, 9)
    b_tuple = (10,)
    print(a_tuple[2])
    print(a_tuple[1:3])
    a = 3
    b = 5
    a, b = swap_val(a, b)


def exceptions():
    height = input("Your height: ")
    weight = input("Your weight: ")

    try:
        a = 5
        b = 3
        print("BMI: ", weight/height**2)
        c = a + b
    except ZeroDivisionError:
        print("Please do not enter 0 as height")
    except TypeError or ValueError:
        print("Invalid types")


def a_func(some_list):
    some_list[0] = 100


def list_swap(x_list, y_list):
    x_list[0] = 100
    x_list, y_list = y_list, x_list



def references():
    a_list = [1, 2, 3, 4, 5]
    b_list = a_list
    #b_list[0] = 100
    #print(a_list)
    c_list = a_list.copy()
    #c_list[0] = 50
    #print(a_list)
    #print(c_list)

    print(a_list == c_list)
    print(a_list is c_list)
    print(a_list is b_list)

    a_func(a_list)
    print(a_list)

    d_list = ["a","b","c"]

    #a_list, d_list = d_list, a_list
    list_swap(a_list, d_list)

    print(a_list)






