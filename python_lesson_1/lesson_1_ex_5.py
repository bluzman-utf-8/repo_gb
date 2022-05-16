alphabet = 'abcdefghijklmnopqrstuvwxyz'


def my_func(let_one, let_two):
    if let_one not in alphabet or let_two not in alphabet:
        return print('Введите английские буквы.')
    return f'Буква "{let_one}" стоит на {alphabet.find(let_one) + 1} месте, а "{let_two}" на {alphabet.find(let_two) + 1} месте.\n' \
            f'Количество букв между ними: {len(alphabet[alphabet.find(let_one) + 1: alphabet.find(let_two)])}.'

if __name__ == '__main__':
    print(
        my_func(
            input('Введите первую букву: ').lower(),
            input('Введите вторую букву: ').lower()
        )
    )


