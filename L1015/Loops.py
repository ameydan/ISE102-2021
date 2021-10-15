'''
count = 0
ogr_not = 0
acc_not = 0
print("Ogrenci notlarını giriniz. Durmak için -1 giriniz")
while ogr_not != -1:
    ogr_not = int(input(str(count+1)+". notu giriniz: "))
    if ogr_not == -1:
        break
    if ogr_not<0 or ogr_not>100:
        print("Lutfen 0 ile 100 arası bir not giriniz")
        continue
    acc_not += ogr_not
    count += 1

if count>0:
    print("Ortalama: ", acc_not/count)
'''

'''
for i in range(5):
    print(i, end=" ")

print()

for i in range(2, 8):
    print(i, end=" ")

print()

for i in range(2, 8, 2):
    print(i, end=" ")


print()

for i in range(8, -10, -3):
    print(i, end=" ")

print()

for ch in "Tolga Ovatman":
    print(ch,end="-")
'''
'''
for i in range(2):
    for j in range(3):
        print((i*j)+j, end=" ")
    for k in range(2,-1,-1):
        print((i*j)+j, end=" ")

for i in range(5):
    for j in range(5-i):
        print('*',end=" ")
    print()


for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print()    
'''

import random

val = random.randint(1, 100)

print("1-100 arası bir sayi tuttum. ")
guess = 0
count = 0
while guess != val:
    guess = int(input("Tahmininiz? "))
    count += 1
    if guess>val:
        print("Tuttuğum sayı daha küçük")
    elif guess<val:
        print("Tuttuğum sayı daha büyük")
    else:
        print("Tahmininiz dogru")

print("Tebrikler",count,"kerede bildiniz!!")