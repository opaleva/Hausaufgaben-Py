from random import choice


def search_nums(arr, target):
    x = choice(arr)
    y = target - x
    if y in arr:
        print(f'{target} = {x}(arr[{arr.index(x)}]) + {y}(arr[{arr.index(y)}])')
    else:
        search_nums(arr, target)


def main():
    arr = [11, 13, 15, 19]
    target = int(input('Сумма (24, 26, 28, 30, 32 или 34): '))

    search_nums(arr, target)


if __name__ == '__main__':
    main()
