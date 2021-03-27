from typing import TextIO
from itertools import groupby
from random import choice


def text_file_processing(file: TextIO) -> None:
    lines: list[str] = file.readlines()
    line: str = ''.join([a[0] for a in groupby(lines)])
    print(line, end='')


def check_parentheses(parentheses_line: str) -> bool:
    count = 0
    for i in parentheses_line:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def main():
    with open('text.txt', 'w', encoding='utf-8') as file:
        words: list[str] = ['Здравствуй\n', 'Вселенная\n']
        for _ in range(20):
            file.write(choice(words))
    with open('text.txt', encoding='utf-8') as file:
        text_file_processing(file)

    parentheses_set: list[str] = ['(', ')']
    parentheses_line: str = ''.join([choice(parentheses_set) for _ in range(6)])
    print(parentheses_line)
    print(check_parentheses(parentheses_line))
    print(f'(()(())())\n{check_parentheses(parentheses_line="(())")}')


if __name__ == '__main__':
    main()
