def invers_numb(numb):
    return f"Ваше число в обратном порядке: {str(numb)[::-1]}"

if __name__ == '__main__':
    print(invers_numb(int(input('Введите число: '))))

