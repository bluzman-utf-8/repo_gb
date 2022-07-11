from random import randint


# сложность O(n**2). устойчивая сортировка
def insert_sort(spisok):
    print(f'Неотсортированный список: {spisok}')
    for i in range(1, len(spisok)):
        key = spisok[i]
        j = i - 1
        while spisok[j] > key and j >= 0:
            spisok[j + 1] = spisok[j]
            j -= 1
        spisok[j + 1] = key
    return spisok


if __name__ == '__main__':
    s = [randint(0, 50) for i in range(10)]
    print(f'Отсортированный список: {insert_sort(s)}')
