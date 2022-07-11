from random import randrange

m = int(input('Размер массива - 2m + 1. Введите m: '))

us_mass = [randrange(100) for i in range((m * 2) + 1)]
mid_el = us_mass[len(us_mass) // 2]
print(mid_el)
res_left = []
res_right = []
midls = []
for i in us_mass:
    if i > mid_el:
        res_right.append(i)
    elif i < mid_el:
        res_left.append(i)
    else:
        midls.append(i)

res = res_left + midls + res_right

print(us_mass)
print(res)

# Решение без сортировки, совсем не элегантное