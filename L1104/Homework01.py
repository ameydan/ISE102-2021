import random


def question01():
    print("********* Homework question 1*********")
    throw1 = random.randint(1, 6)
    throw2 = random.randint(1, 6)
    acc = throw1 + throw2
    while throw1 == throw2:
        throw1 = random.randint(1, 6)
        throw2 = random.randint(1, 6)
        acc = acc + throw1 + throw2

    print(acc)
    print("*********Homework question 1*********\n")


def question02():
    print("*********Homework question 2*********")
    P0 = float(input("Input budget: "))
    i = float(input("Interest rate: "))
    goal = float(input("Input targer budget: "))

    count = 0
    Pn = P0
    while Pn < goal:
        Pn = (1+i)*Pn
        count += 1

    print("Reached", Pn, "after", count, "iterations")
    print("*********Homework question 2*********\n")
