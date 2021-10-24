import math

def variable_declaration():
    print("*********Declaring Variables*********")
    var = math.ceil(5/2)
    print(var)
    print("*********Declaring Variables*********\n")


def take_input():
    print("*********Reading Input*********")
    var = input("Input some string: ")
    print(var)
    print("*********Reading Input*********\n")


def formatting_print():
    print("*********Formatting Printing*********")
    print("Tolga", "Ovatman", sep="--", end="")
    print("Merhaba")
    var = "Merhaba{0}Tolga{1}Ovatman"
    print(var.format("--", "**"))
    print("*********Formatting Printing*********\n")