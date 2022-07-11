def operation_for_numbs(numb_1, numb_2, operator):
    if operator == '+':
        return f'Результат сложения: {numb_1 + numb_2}'
    elif operator == '-':
        return f'Результат вычитания: {numb_1 - numb_2}'
    elif operator == '*':
        return f'Результат умножения: {numb_1 * numb_2}'
    elif operator == '/':
        if numb_2 == 0:
            return '0'
        return f'Резултат деления: {numb_1 / numb_2}'
    elif operator == '0':
        return 'Выход'
    return False


if __name__ == '__main__':
    while True:
        res = operation_for_numbs(
            int(input('Введите первое число: ')),
            int(input('Введите второе число: ')),
            input('Выберите операцию - "+", "-", "*" или "/", для выхода введите 0: ')
        )

        if res == 'Выход':
            break
        elif res == False:
            print('Введены неверное значение')
            print('')
            continue
        elif res == '0':
            print('На 0 делить нельзя!')
            print('')
            continue

        print(res)
        print('')