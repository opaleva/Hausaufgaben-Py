from typing import TextIO, Union
from random import randint
from collections import Counter
import re


def count_unique_elements(arr: Union[list[str], list[int]]) -> int:
    return len(set(arr))


def get_10_popular_password(file: TextIO) -> None:
    strings: list[str] = file.readlines()
    strings = [string[string.find(";") + 1:-1] for string in strings]
    numbers_list: list[int] = [i for i in range(len(strings))]
    dictionary: dict[int, str] = dict(zip(numbers_list, strings))
    count: list[tuple[str, int]] = Counter(dictionary.values()).most_common(10)
    for item in count:
        print(item)


# По-хорошему ссылки лучше проверять через BeautifulSoup на предмет их "работоспособности".
# Но раз по условию подразумевается, что они все рабочие и их надо просто заменить, то сгодится и простой regex.
def censor_link(link: str) -> str:
    a: str = re.sub(r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '*****', link)
    return a


def main():
    lists: list[Union[list[str], list[int]]] = [['abc', 'abb', 'ab', 'abc', 'abd'],
                                                [randint(1, 15) for _ in range(20)]]
    for arr in lists:
        print(f'{sorted(arr)} –> {count_unique_elements(arr)} различных элементов.')

    with open('pwd.txt') as file:
        print('\nСамые используемые пароли: ')
        get_10_popular_password(file)

    links: list[str] = ['flightradar24.com',
                        'https://www.flightradar24.com/57.53,26.63/5',
                        'www.flightradar24.com/airport/svo/departures',
                        't1p.de',
                        'https://www.tagesschau.de/',
                        'https://domains.google/',
                        'www.site.com',
                        'http://example.su',
                        'vk.ru',
                        'https://example.com/smth/else']
    for link in links:
        print(censor_link(link))


if __name__ == '__main__':
    main()
