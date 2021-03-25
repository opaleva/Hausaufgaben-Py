from statistics import median
from random import randint
from os import path


def get_median(num1: list[int], num2: list[int]) -> float:
    num1.extend(num2)
    return median(num1)
# Без непосредственного вызова statistics.median:
    # num1.extend(num2)
    # num1.sort()
    # n: int = len(num1)
    # if n % 2 == 1:
    #     return num1[n // 2]
    # else:
    #     i: int = n // 2
    #     return (num1[i - 1] + num1[i]) / 2


def longest_palindrome(s: str) -> str:
    # Здесь вполне уместно использовать Manacher's algorithm, но он слишком уж многословный, поэтому:
    substring: str = ""
    for x in range(len(s)):
        # Для букв в обратном порядке:
        for y in range(len(s), x, -1):
            if s[x:y] == s[x:y][::-1]:
                if len(substring) < len(s[x:y]):
                    substring = s[x:y]
    return substring


def longest_common_prefix(strings: list[str]) -> str:
    return path.commonprefix(strings)
# Без непосредственного вызова path.commonprefix:
#     for number, letters in enumerate(zip(*strings)):
#         if len(set(letters)) > 1:
#             return strings[0][:number]
#         else:
#             return min(strings)


def main():
    num1: list[int] = [randint(1, 100) for _ in range(20)]
    num2: list[int] = [randint(1, 100) for _ in range(20)]
    print(f'{sorted(num1)}\n{sorted(num2)}\n–> {get_median(num1, num2)}\n')

    while True:
        s: str = input("Строка для проверки (exit для выхода):\n")
        if s == "exit":
            break
        print(longest_palindrome(s))

    lists: tuple[list[str], list[str]] = ["flower", "flow", "flight"], ["dog", "airplane", "plane"]
    print()
    for strings in lists:
        print(f'{strings} –> "{longest_common_prefix(strings)}"')


if __name__ == '__main__':
    main()
