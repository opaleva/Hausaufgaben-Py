def translate_to_bytes_or_kilobytes(num, metric):
    if metric == 'k':
        print(f'В {num} байтах – {divmod(num, 1024)} килобайтов.')
    elif metric == 'b':
        print(f'В {num} килобайтах – {num * 1024} байтов.')
    else:
        print('Неверный запрос')


def get_greatest_numeral(number):
    max_digit = max([i for i in str(number)])
    print(f'Наибольшая цифра в числе {number} – {max_digit}.')


def get_nums(arr):
    x = len(arr)
    average = sum(arr) / x
    under_average = []
    for i in range(x):
        if arr[i] < average:
            under_average.append(arr[i])
    print(f'Числа меньше среднего арифметического ({average}) – {", ".join(str(i) for i in under_average)}')


def main():
    metric = input('Во что переводить? k – Kbyte, b – byte: ')
    try:
        num = int(input('Сколько переводить? '))
        translate_to_bytes_or_kilobytes(num, metric)

        number = int(input('Произвольное число: '))
        get_greatest_numeral(number)
    except ValueError:
        print('Не является числом.')

    arr = []
    print('Целое число для массива (буква либо знак – окончание заполнения):')
    while True:
        try:
            user_input = int(input())
        except ValueError:
            break
        arr.append(user_input)
    get_nums(arr)


if __name__ == '__main__':
    main()
