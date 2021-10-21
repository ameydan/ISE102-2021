import random
'''
print("Please think of a number between 1-100")

low_bound = 1
high_bound = 100
guess = random.randint(low_bound, high_bound)
print("I guess,", guess)

while True:
    print("Should I guess (L)ower/(H)igher, or did I guess (C)orrect? ")
    high_low = input()

    if high_low == "C":
        print("Correct!!!")
        break
    elif high_low == "L":
        high_bound = guess - 1
        guess = random.randint(low_bound, high_bound)
    elif high_low == "H":
        low_bound = guess + 1
        guess = random.randint(low_bound, high_bound)

    print("I guess,", guess)
    
'''
'''
num = 1
minnum = 100000
maxnum = -100000
while num != -1:
    num = int(input())
    if num == -1:
        break
    if num < minnum:
        minnum = num
    if num > maxnum:
        maxnum = num

print("Minimum number so far", minnum)
print("Maximum number so far", maxnum)
'''
'''
height = int(input("Enter height "))

for i in range(height):
    for j in range(5-i-1):
        print(' ',end="")
    for k in range(2*i+1):
        print('*',end="")
    print()



for i in range(height):
    low = (2*height-1)//2
    high = (2*height-1)//2
    for j in range(2*height-1):
        if (low-i) <= j <= (high+i):
            print('*',end='')
        else:
            print(' ',end='')
    print()

'''

num = int(input("Input a number "))

while num // 10 != 0:
    print(num%10,end="")
    num = num // 10
else:
    print(num % 10)


