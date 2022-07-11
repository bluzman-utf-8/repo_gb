import collections

amount_comp = int(input('Введите количество предприятний: '))

n = 0
companies = {}

while n != amount_comp:
    info_comp = input('Введите наименование комании и прибыль за 4 квартала (т.е. 4 отдельных числа). Всю информацию вводите через пробел: ').split(' ')
    companies[info_comp[0]] = sum(map(int, info_comp[1:]))
    n += 1

counter = collections.Counter(companies)

comps_with_profit = [i for i in counter.keys() if companies[i] > (sum(counter.values()) / len(counter.keys()))]
comps_with_not_profit = [i for i in counter.keys() if companies[i] < (sum(counter.values()) / len(counter.keys()))]

print(f'Средняя прибыль за год всех предприятий: {sum(counter.values()) / len(counter.keys())} рублей')
print("Компании с прибылью выше среднего: " + str(comps_with_profit).replace("[", "").replace("]", "").replace("'", ""))
print()
print("Компании с прибылью ниже среднего: " + str(comps_with_not_profit).replace("[", "").replace("]", "").replace("'", ""))


# Сложность алгоритма O(n*n)