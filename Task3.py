# Task3
from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(-100, 100))
print(a)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)