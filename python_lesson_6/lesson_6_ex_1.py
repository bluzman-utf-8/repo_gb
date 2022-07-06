from sys import getsizeof
## Версия python 3.9.7, 64-разрядная система, MacBook Pro M1

# Задача 2 из 2 урока
even_numbs = []
odd_numbs = []

def my_func(numb):
    for i in numb:
        if int(i) % 2 == 0:
            even_numbs.append(i)
        else:
            odd_numbs.append(i)
    print(f'Под переменную even_numbs выделено {getsizeof(even_numbs)} байт.')
    print(f'Под переменную odd_numbs выделено {getsizeof(odd_numbs)} байт.')
    print(f'Под переменную i выделено {getsizeof(i)} байт.')
    return f'Количесво четных цифр: {len(even_numbs)}, нечетных: {len(odd_numbs)}'

if __name__ == '__main__':
    print(
        my_func(input('Введите натуральное число: '))
    )
# В данной задаче вместе словарей можно было бы использовать множества(set()),
# так как они занимают меньше памяти, чем словари
# Пространственная сложность данного алгоритма O(n) - учитываем информацию, которю вводит пользователь



# Задача 1 из 3 урока

res = {2: 0,
       3: 0,
       4: 0,
       5: 0,
       6: 0,
       7: 0,
       8: 0,
       9: 0}

for i in range(2, 100):
    for n in range(2, 10):
        if i % n == 0:
            res[n] += 1
        else:
            continue

for key, val in res.items():
    print(f'Количество чисел, кратные {key} из последовательности от 2 до 99 равно: {val}')

print(f'Под переменную "res" выделено {getsizeof(res)} байт.')
print(f'Под переменную "key" выделено {getsizeof(key)} байт.')
print(f'Под переменную "val" выделено {getsizeof(val)} байт.')
## Под словарь будет выделяться 360 байт, под key и val по 28 байта, так как их значения на каждной итерации
# равны по одному числу
# Пространственная сложность данного алгоритма O(1)- так как данные у нас фиксированные