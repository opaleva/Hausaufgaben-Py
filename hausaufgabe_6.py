from functools import reduce
import random
import string
from textwrap import wrap


# Задача на reduce и filter
def sum_numbers(arr: list[int]) -> int:
    return reduce(lambda x, y: x + y, filter(lambda x: x % 2 != 0 and x <= 11, arr))


# Задача на map
def set_title(alphabet: list[str]) -> list[str]:
    return list(map(str.title, alphabet))


# Задача на рекурсию
def determine_power(n: float) -> str:
    if n == 1:
        return f'является степенью числа 2.'
    elif n < 1:
        return f'не является степенью числа 2.'
    else:
        return determine_power(n / 2)


def main():
    try:
        arr = [random.randint(0, 20) for _ in range(7)]
        print(arr)
        print(f'Сумма нечётных чисел, меньших либо равных 11, = {sum_numbers(arr)}\n')
    except TypeError:
        print('В данном списке все числа больше 11.')

    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
    alphabet = wrap(letters, 4)
    print(alphabet)
    print(" - ".join(set_title(alphabet)), '\n')

    n = random.randint(1, 10000)
    print(f'Число {n} {determine_power(n)}')
    n = 32
    print(f'Число {n} {determine_power(n)}')


if __name__ == '__main__':
    main()
