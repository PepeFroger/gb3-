# Task5
print("Количество заказов: ", end="")
count = int(input())

direct = dict()

for i in range(count):
    name, pizza, num = input(f" {i+1} заказ: ").split()
    num = int(num)
    if name not in direct:
        direct[name] = {pizza: num}
    elif pizza in direct:
        direct[name][pizza] += num
    else:
        direct[name][pizza] = num

for i in sorted(direct.keys()):
    print(f'{name}:')
for pizza_name in sorted(direct[name].keys()):
    print(f' {pizza_name}: {direct[name][pizza]}')