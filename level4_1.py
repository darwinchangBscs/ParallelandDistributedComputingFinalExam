import random

randomlist = []

for i in range(0,100):
    n = random.randint(0,999)
    randomlist.append(n)
    randomlist.sort()
print("A. Random Numbers : ", "\n", randomlist)

print("\n")
print("B. Even Numbers : ")
for num in randomlist:
    if num % 2 == 0:
        print(num,", ",end="")

print("\n")
print("B. Odd Numbers : ")
for num in randomlist:
    if num % 2 != 0:
        print(num,", ",end="")

print("\n")
print("C. Numbers Divisible by 9 : ")
for num in randomlist:
    if num % 9 == 0:
        print(num,", ",end="")

print("\n")
print("D. Prime Numbers : ")
for num in randomlist:
    for i in range(2, num//2):
        if (num % i) == 0:
            break
        else:
            print(num,", ",end="")
            break
                 

   

print("\n")
print("E. Numbers Contains 9 : ")
for num in randomlist:
    if '9' in str(num):
        print(num,", ",end="")






