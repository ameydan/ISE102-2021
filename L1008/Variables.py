import math

def variable_declaration():
    print("*********Declaring Variables*********")
    var = math.ceil(5/2)
    print(var)


def take_input():
    print("*********Taking Input*********")
    var = input()
    print(var)


def formatting_print():
    print("*********Formatting Printing*********")
    print("Tolga", "Ovatman", sep="--", end="")
    print("Merhaba")
    var = "Merhaba{0}Tolga{1}Ovatman"
    print(var.format("--", "**"))