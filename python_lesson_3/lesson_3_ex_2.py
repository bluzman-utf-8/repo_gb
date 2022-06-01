from random import randint

user_val = int(input('Программа составит список из рандомных чисел от 0 до 100. Введите длинну списка: '))
mas = [randint(0, 100) for i in range(user_val)]
res = [k + 1 for k, v in enumerate(mas) if v % 2 == 0]

print(f'Вот как список у вас получился: {mas}.\nА вот список с индексами только четных чисел, нумерация начинается с цифры 1: {res}')