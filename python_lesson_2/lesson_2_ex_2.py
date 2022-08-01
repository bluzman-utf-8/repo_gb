even_numbs = []
odd_numbs = []

def my_func(numb):
    for i in numb:
        if int(i) % 2 == 0:
            even_numbs.append(i)
        else:
            odd_numbs.append(i)
    return f'Количесво четных цифр: {len(even_numbs)}, нечетных: {len(odd_numbs)}'

if __name__ == '__main__':
    print(
        my_func(input('Введите натуральное число: '))
    )