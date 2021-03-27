import collections
import random


def get_max_freq_num(arr):
    x = collections.Counter(arr)
    for number, counter in x.most_common(1):
        if counter > 1:
            print(f'В массиве {arr} число {number} встречается чаще всего: {counter} раз(а).')
        else:
            print(f'В массиве {arr} нет повторяющихся чисел.')


def main():
    arr = [random.randint(1, 20) for _ in range(15)]
    get_max_freq_num(arr)


if __name__ == '__main__':
    main()
