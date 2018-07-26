import random
import time

a = random.randint(1,9)
a = int(a)

b = random.randint(1,9)
b = int(b)

c = random.randint(1,9)
c = int(c)

d = random.randint(1,9)
d = int(d)

e = random.randint(1,9)
e = int(e)

f = random.randint(1,9)
f = int(f)

p = (a,b,c,d,e,f)
print(p)

ls = input()
ls = int(ls)

if ls == p:
    print("correct")
elif ls != p:
    print("incorrect")
