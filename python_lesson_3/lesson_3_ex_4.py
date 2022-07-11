from random import randint

user_val = int(input('Программа составит список из рандомных чисел от 0 до 5. Введите длинну списка: '))
mas = [randint(0, 5) for i in range(user_val)]
print(f'Получился такой список: {mas}')

unic_el = set(mas)
print(f'Элемент, который встречается больше всего: {max(i for i in unic_el if mas.count(i) == max(map(mas.count, mas)))}')
