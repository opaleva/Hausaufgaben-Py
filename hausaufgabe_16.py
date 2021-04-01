from random import randint


def length_of_longest_substring(string: str) -> int:
    length = 0
    first_index = 0
    substring = {}
    for i in range(0, len(string)):
        if string[i] in substring:
            first_index = max(first_index, substring[string[i]] + 1)
        length = max(length, i - first_index + 1)
        substring[string[i]] = i
    return length


# Алгоритм Кадане с указанием искомой подстроки.
def max_sub_array(nums: list[int]) -> tuple[int, ...]:
    length = 0
    first_number = last_number = 0
    current_sum, current_start = 0, 0
    for current_end, x in enumerate(nums):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x
        if current_sum > length:
            length = current_sum
            first_number = current_start
            last_number = current_end + 1
    return length, first_number, last_number


def main():
    while True:
        string: str = input("Строка для проверки (exit для выхода):\n")
        if string == "exit":
            break
        print(f'Длина наибольшей подстроки без повторов: {length_of_longest_substring(string)} симв.')

    for _ in range(5):
        nums = [randint(-20, 20) for _ in range(10)]
        print(f'{nums} –> Сумма: {max_sub_array(nums)[0]}, '
              f'в интервале nums[{max_sub_array(nums)[1]}] – nums[{max_sub_array(nums)[2] - 1}] включительно.')


if __name__ == '__main__':
    main()
