# Урок 2, задание 3
# Способ 1
import time

def invers_numb(numb):
    return f"Ваше число в обратном порядке: {str(numb)[::-1]}" #Сложность O(1)


if __name__ == '__main__':
    user_data = int(input('Введите число: '))

    time_s = time.time()
    a = invers_numb(user_data)
    time_f = time.time()

    print(f'Ваше число в обратном порядке: {a}')
    print(f'Скорость первого алгоритма: {time_f - time_s} сек')

# Способ 2 Сложность O(n)

def invers_numb_two(numb):
    res = ''
    for i in str(numb):
        res = i + res
    return res

if __name__ == '__main__':
    user_data = int(input('Введите число: '))

    time_s = time.time()
    a = invers_numb_two(user_data)
    time_f = time.time()

    print(f"Число в обратном порядке: {a}")
    print(f'Скорость второго алгоритма {time_f - time_s}')

# При маленьких входных данных результат работы алгоритмов практически равен, при большин - очевидно, выигрывает первый алгоритм