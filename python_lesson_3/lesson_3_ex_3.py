from random import randint

user_val = int(input('Программа составит список из рандомных чисел от 0 до 100. Введите длинну списка: '))
mas = [randint(0, 100) for i in range(user_val)]
print(f'Получился такой список: {mas}')
indx_min_el = mas.index(min(mas))
indx_max_el = mas.index(max(mas))

mas[indx_min_el], mas[indx_max_el] = mas[indx_max_el], mas[indx_min_el]

print(f'Поменяли местами минимальный и максимальный элементы: {mas}')