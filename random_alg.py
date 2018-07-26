import random
import time

ls = random.randint(100000,999999)
print(ls)
print("guess")
l = input()
l = str(l)

if l == ls:
    ls = str(ls)
    print("correct, good job!")

elif l != ls:
    print("wrong")
