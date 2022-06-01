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