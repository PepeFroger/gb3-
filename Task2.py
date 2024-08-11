# Task2
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']
print("Количество фильмов: ", end="")
count = int(input())
a = []
for i in range(count):
    print("Введите название фильма: ", end="")
    name = str(input())
    if name in films:
        a.append(name)
    else:
        print(f"Ошибка: фильма {name} у нас нет :(")
print(f"Ваш список любимых фильмов: {a}")