for i, n in enumerate(range(32, 128), 1):
    print(f'Код: {n} Символ: {chr(n)}', end=' ')
    if i % 10 == 0:
        print()
