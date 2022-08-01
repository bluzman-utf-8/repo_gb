# С использованием алгоритма Решето Эратосфена
# Сложность алгоритма O(n)
import time

j = int(input('Какое по счету просто число вы хотите узнать? Введите порядковый номер до 1229: '))

time_s = time.time()

prost_set = []
n = 10000
sieve = set(range(2, n + 1))
while sieve:
    if len(prost_set) == j:
        break
    else:
        prime = min(sieve)
        prost_set.append(prime)
        sieve -= set(range(prime, n + 1, prime))

time_f = time.time()

print(f'Это число: {prost_set[j - 1]}')
print(f'Скорость алгоритма: {time_f - time_s} c')
print()

# Без использования алгоритма Решето Эратосфена
# Сложность алгоритма O(n**2)
print('Ниже использован алгоритм без использования алгоритма Решето Эратосфена')
print()
j = int(input('Какое по счету просто число вы хотите узнать? Введите порядковый номер до 1229: '))

time_s = time.time()

prost_set = []
n = 10000
sieve = set(range(2, n + 1))

for i in sieve:
    dividers = []
    for g in range(1, i + 1):
        if i % g == 0:
            dividers.append(g)
    if len(dividers) == 2:
        prost_set.append(i)

time_f = time.time()

print(f'Это число: {prost_set[j - 1]}')
print(f'Скорость алгоритма {time_f - time_s} с')





