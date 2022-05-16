from random import randint, uniform, choice

symb_in_str = 'abcdefghijklmnopqrstuvwxyz'


def my_generator(type, start, stop):
    if type == 'i':
        return f'Случайно целое число в заданном вами диапазоне: {randint(int(start), int(stop))}'
    elif type == 'f':
        return f'Случайно вещественное число в заданном вами диапазоне: {round(float(uniform(float(start), float(stop))), 3)}'
    elif type == 's':
        return f'Случайный символ в заданном вами диапазоне: {choice(symb_in_str[symb_in_str.find(start): symb_in_str.find(stop) + 1])}'
    raise Exception('Введены неккоректные значение')


if __name__ == '__main__':
    print(
        my_generator(
            input('Выберите тип диапозона: "i" - целое число; "f" - вещественное число; "s" - символ: '),
            input('Введите начало диапозона: '),
            input('Введите конец диапозона: ')
        )
    )
