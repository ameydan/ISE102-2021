import math

def gcd(a, b):
    while True:
        buyuk = max(a, b)
        kucuk = min(a, b)

        kalan = buyuk % kucuk
        if kalan == 1:
            return 1
        if kalan == 0:
            return kucuk

        a = kalan
        b = kucuk


def stdev():
    print("Input grades, -1 to stop")

    grades = []
    while True:
        grades.append(int(input()))
        if grades[-1] == -1:
            del grades[-1]
            break

    avg = sum(grades)/len(grades)

    sum_square = sum([(i-avg)**2 for i in grades])
    #for i in grades:
    #    sum_square += (i-avg)**2

    print(math.sqrt(sum_square/len(grades)))


def dot_product():
    inp1 = input("Enter vector 1: ")
    inp2 = input("Enter vector 2: ")

    v_1 = [int(s) for s in inp1.split()]
    v_2 = [int(s) for s in inp2.split()]

    if len(v_1) != len(v_2):
        return

    dot_pro = 0
    #for i in range(len(v_1)):
    #    dot_pro += v_1[i]*v_2[i]

    for tup in zip(v_1, v_2):
        dot_pro += tup[0]*tup[1]

    print(dot_pro)

def read_matrix():
    matrix = []
    print("Enter rows of matrix")
    while True:
        inp1 = input()
        if inp1 == 'q':
            break
        matrix.append([int(s) for s in inp1.split()])

    return matrix

def print_transpose(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("("+str(i)+","+str(j)+")", end=" ")
        print()
    # This code is not yet completed

def test_gcd():
    print("********* GCD Exercise *********")
    print("GCD 47 96:", gcd(47,96))
    print("GCD 42 96:", gcd(42,96))
    print("********* GCD Exercise *********\n")

def test_stdev():
    print("********* STDEV Exercise *********")
    stdev()
    print("********* STDEV Exercise *********\n")


def test_dot_product():
    print("********* Vector dot product Exercise *********")
    dot_product()
    print("********* Vector dot product Exercise *********"\n)

def test_read_matrix():
    print("********* Read matrix Exercise *********")
    read_matrix()
    print("********* Read matrix Exercise *********\n")

def test_print_transpose():
    print("********* Transpose matrix Exercise *********")
    print_transpose([[1, 2, 3],[4, 5, 6]])
    print("********* Transpose matrix Exercise *********\n")
