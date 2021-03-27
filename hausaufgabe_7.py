from typing import List, Tuple, Set
import string
import re
from functools import reduce

# Задача 1
# В месяце 30 дней => в году 30 * 12 = 360 дней
# def get_days(date: List[int], multipliers: Tuple[int, ...]) -> int:
#     return sum(x * y for x, y in zip(date, multipliers))


# Задача 2
# def get_number(x: str, y: str) -> str:
#     return x[:2] + y[:2]


# Задача 3
def get_sum(text: list[str], numbers: dict[int, str]) -> int:
    return reduce(lambda x, y: x + y, filter(lambda x: numbers[x] in text, numbers))


def main():
    # try:
    #     date: List[int] = [int(i) for i in input('Количество недель, месяцев, лет (через пробел):\n ').split()]
    #     multipliers: Tuple[int, ...] = (7, 30, 360)
    #     print(get_days(date, multipliers), 'дней.\n')
    #
    #     x, y = input('Два трёхзначных числа через пробел:\n ').split(' ')
    #     if re.match(pattern=r"^\d{3}$", string=x):
    #         if re.match(pattern=r"^\d{3}$", string=y):
    #             print(int(get_number(x, y)))
    # except ValueError:
    #     print('Это какие-то неправильные числа. Или невидимые.')

    text = '''
            один три два семь девять четыре пять восемь шесть'''
    print(text)
    # text = list(text.lower().translate(str.maketrans('', '', string.punctuation)).split(' '))
    numbers: dict[int, str] = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
                               6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}

    print(get_sum(text, numbers))


if __name__ == '__main__':
    main()
