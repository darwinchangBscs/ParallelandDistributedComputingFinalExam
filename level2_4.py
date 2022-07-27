import random

num = 1

while num<=50:
    if (num % 3) == 0 or (num % 4) == 0 or (num % 5) == 0:
        print(num,",", end="")
    num = num + 1