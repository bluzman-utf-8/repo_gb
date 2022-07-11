from random import randint


# сложность O(n**2). устойчивая сортировка
def bubble_sort(spisok):
    print(f'Неотсортированный список: {spisok}')
    swapped = False  # текущее действие
    for i in range(len(spisok) - 1, 0, -1):
        for j in range(i):
            if spisok[j] < spisok[j + 1]:  # Меняем знак
                spisok[j + 1], spisok[j] = spisok[j], spisok[j + 1]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return spisok


if __name__ == '__main__':
    s = [randint(-100, 100) for i in range(10)]
    print(f'Отсортированный список: {bubble_sort(s)}')
