def func_numbs(numb, operator):
    if operator == 'sum':
        return f'Сумма цифр равна {sum(map(int, str(numb)))}'
    elif operator == 'mul':
        m = 1
        while numb > 0:
            m *= numb % 10
            numb = numb // 10
        return f'Произведение цифр равно {m}' # либо return f'Произведение цифр равно {int(str(numb)[0]) * int(str(numb)[1]) * int(str(numb)[-1])}'
    raise Exception('Упс! Введены некоректные значения.')


if __name__ == '__main__':
    print(
        func_numbs(
            int(input('Введите трехзначное число: ')),
            input('Введите "sum", чтобы сложить цифры числа или "mul", чтобы перемножить: ')
        )
    )