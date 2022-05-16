def equation_line(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return f'Уравнение прямой: y = {k}x + {b}'

if __name__ == '__main__':
    print(
        equation_line(
            int(input('Введите x1: ')),
            int(input('Введите y1: ')),
            int(input('Введите x2: ')),
            int(input('Введите y2: '))
        )
    )