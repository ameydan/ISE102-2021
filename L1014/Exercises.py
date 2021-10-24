def calculate_bmi():
    print("*********BMI calculation*********")
    kilo = int(input("Kilonuzu giriniz (kg)"))
    boy = float(input("Boyunuzu giriniz (m)"))

    print("BMI degeri", kilo/boy**2)
    print("*********BMI calculation*********\n")


def transform_temperature():
    print("*********Transform Temperature*********")
    degree = float(input("Sıcaklık degeri giriniz "))
    cf = input("Celicus için C, Fahrenheit için F giriniz ")
    if cf == "C":
        print(degree*1.8+32, " F")
    elif cf == "F":
        print((degree-32)/1.8, " C")
    else:
        print("C/F olmalı")
    print("*********Transform Temperature*********\n")


def ascending_descending():
    print("*********Three numbers ascending/descending?*********")

    num_1 = int(input("İlk sayıyı giriniz "))
    num_2 = int(input("İkinci sayıyı giriniz "))
    num_3 = int(input("Ucuncu sayıyı giriniz "))

    if num_1>num_2>num_3:
        print("Azalan sıra")
    elif num_1<num_2<num_3:
        print("Artan sıra")
    else:
        print("Hicbiri")

    print("*********Three numbers ascending/descending?*********\n")

def ascending_descending_2():
    print("*********Three numbers ascending/descending? v2*********")

    num_1 = int(input("İlk sayıyı giriniz "))
    num_2 = int(input("İkinci sayıyı giriniz "))
    num_3 = int(input("Ucuncu sayıyı giriniz "))

    if num_1 <= num_2 and num_1 <= num_3:
        if num_2 <= num_3:
            print(num_1, num_2, num_3)
        else:
            print(num_1, num_3, num_2)
    elif num_2 <= num_3 and num_2 <= num_1:
        if num_1 <= num_3:
            print(num_2, num_1, num_3)
        else:
            print(num_2, num_3, num_1)
    else:
        if num_2 <= num_1:
            print(num_3, num_2, num_1)
        else:
            print(num_3, num_1, num_2)
    print("*********Three numbers ascending/descending? v2*********\n")

def leap_year():
    print("*********Leap year*********")

    yil = int(input("Bir yıl degeri giriniz "))

    if yil%4==0:
        if yil%100==0:
            if yil%400==0:
                print("Artık yıl")
            else:
                print("Artık yıl degil")
        else:
            print("Artık yıl")
    else:
        print("Artık yıl degil")
    print("*********Leap year*********\n")
