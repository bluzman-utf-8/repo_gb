def sum_numbs(n):
    m = 1
    res = []
    for i in range(n - 1):
        if i == 0:
            res.append(m)
        res.append(m / -2)
        m /= -2
    return f'Сумма элементов последовательности: 1; -0.5; 0.25; -0.125;... равна: {sum(res)}'

if __name__ == '__main__':
    print(sum_numbs(int(input('Введите количество элементов: '))))
