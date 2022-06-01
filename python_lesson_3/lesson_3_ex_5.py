from random import randint

user_val = int(input('Программа составит список из рандомных чисел от 0 до 5. Введите длинну списка: '))
mas = [randint(-100, 5) for i in range(user_val)]
print(f'Получился такой список: {mas}')

print(f'Максимальный отрицательный элемент: {sorted(mas)[0]}, его индекс: {mas.index(sorted(mas)[0])}')

