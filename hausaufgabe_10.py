from typing import List, Union, Dict
from random import randint, choice


def to_dict(lst: List[Union[List[int], List[str]]]) -> None:
    for x in lst:
        print(f'{ {a: a for a in sorted(x)} }')


def count_it(sequence: str) -> None:
    numbers_dict = {}
    for i in sequence:
        if i not in numbers_dict:
            numbers_dict[i] = 1
        else:
            numbers_dict[i] += 1
    numbers_dict = {int(x): y for x, y in sorted(numbers_dict.items())}
    print(numbers_dict, '\n')
    print(set(numbers_dict))


def max_dct(dict1: Dict[str, int], dict2: Dict[str, int]) -> None:
    print(f'{ dict(sorted({x: max(dict1.get(x, 0), dict2.get(x, 0)) for x in set(dict1) | set(dict2)}.items())) }')


def main():
    lst: List[Union[List[int], List[str]]] = [[randint(1, 9) for _ in range(10)],
                                              ['a', 'е', 'b', 'c', 'ж', 'd', 'е', 'з']]
    print(lst[0], end=' –> ')
    to_dict(lst)

    sequence: str = str(randint(pow(10, 20), pow(10, 30)))
    print(f'\n{sequence}', end=' –> ')
    count_it(sequence)

    letters: str = 'qrstuvwxyz'
    dict_1: Dict[str, int] = {choice(letters): randint(1, 9) for _ in range(10)}
    dict_2: Dict[str, int] = {choice(letters): randint(1, 9) for _ in range(10)}
    print(f'{sorted(dict_1.items())}\n{sorted(dict_2.items())}')
    max_dct(dict_1, dict_2)


if __name__ == '__main__':
    main()
