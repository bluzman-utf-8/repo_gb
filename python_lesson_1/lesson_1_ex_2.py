def bit_operations(a, b, operator):
    if operator == 'and':
        return a & b
    elif operator == 'or':
        return a | b
    elif operator == 'xor':
        return a ^ b
    elif operator == 'shift':
        return f'Результат сдвига вправо - {a >> 2}, влево - {a << 2} '
        # При сдвиге вправо - делим число на 4 (или 2 в степени 2), отбрасывая дробную часть, влево - умножаем на 4
    raise Exception('Введены неккоректные данные')

if __name__ == '__main__':
    print(
        bit_operations(
            5,
            6,
            input('Чтобы выполнить побитовые операции введите: "and" - И; "or" - ИЛИ; "xor" - исключающее ИЛИ; '
                  '"shift" - сдвиг право и влево числа 5 на два знака: ')
        )
    )
