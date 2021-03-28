from typing import Generator
from random import randint


# Генератор + yield вместо return – самое то для создания списков :)
# Чтобы не перегружать функцию – преобразование в строку вынесено в main.
def get_fib(n: int) -> Generator[int, None, None]:
    if n > 0:
        yield 1
    first: int = 0
    second: int = 1
    for _ in range(1, n):
        first, second = second, first + second
        yield second


def get_index(nums: list[int], target: int) -> int:
    nums.append(target)
    return sorted(nums).index(target)


# Если пропущено именно одно число, то находится через разность сумм.
# Если несколько – то через приведение к set и нахождение set1^set2.
def get_skipped_num(numbers: list[int]) -> int:
    return sum(x for x in range(1, 101)) - sum(numbers)


def main():
    try:
        print(", ".join(map(str, list(get_fib(int(input("Количество чисел в последовательности: ")))))))

        nums: list[int] = list({randint(1, 20) for _ in range(15)})
        print(f'\n{sorted(nums)}')
        target: int = int(input("Число: "))
        print(f'{target} –> nums[{get_index(nums, target)}]\n')

        numbers: list[int] = [i for i in range(1, 101)]
        numbers.remove(randint(1, 100))
        print(numbers)
        print(f'Пропущено число {get_skipped_num(numbers)}.')

    except ValueError:
        print('Это не число.')


if __name__ == '__main__':
    main()
