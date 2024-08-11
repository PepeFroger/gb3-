# Task 1
print("Количество видеокард: ", end="")
count = int(input())
a = []
b = []
for i in range(count):
    print(f"Видеокарта {i+1}: ", end="")
    num = int(input())
    a.append(num)
imax = a[0]
for i in a:
    if i> imax:
        imax = i

for i in a:
    if i != imax:
        b.append(i)
print(f"Старый список: {a}", f"Новый список: {b}", sep="\n")
