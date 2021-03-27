import string


# Задача 1
def count_numbers(a, b):
    if a < b:
        count_numbers(a, b - 1)
        print(b, end=' ')
    elif a > b:
        count_numbers(a - 1, b)
        print(a, end=' ')
    else:
        print(a, end=' ')


# Задача 2
def count_letters(text):
    letters = {}
    for char in text:
        if char in string.whitespace or char in string.punctuation:
            continue
        char = char.upper()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    # Обратная сортировка словаря по значениям:
    letters = {x: y for x, y in sorted(letters.items(), key=lambda item: item[1], reverse=True)}
    # Сортировка словаря по ключам:
    # letters = {x: y for x, y in sorted(letters.items())}
    return letters


def main():
    try:
        a, b = input('А и В через пробел: ').split(' ')
        a, b = int(a), int(b)
        count_numbers(a, b)
    except ValueError:
        print('Данные символы числом не являются.')

    text = '\n\n\t"Es ist nicht genug zu wissen - man muss auch anwenden. Es ist nicht genug zu wollen - man muss auch tun."'
    print(text, '(Johann Wolfgang von Goethe)\nIn diesem Zitat gibt es:')
    print(count_letters(text))


if __name__ == '__main__':
    main()

# {randint(0, 2)}{randint(0, 9)}:{randint(0, 9)}{randint(0, 9)}:' \
#                      f'{randint(0, 9)}{randint(0, 9)}